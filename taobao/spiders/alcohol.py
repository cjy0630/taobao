# -*- coding: utf-8 -*-
import json
import random
import time

import scrapy

from taobao.config.config_operate import get_cookie, get_search_api, get_keyword, get_comment_api
from taobao.items import TaobaoItem


class AlcoholSpider(scrapy.Spider):
    name = 'alcohol'
    # allowed_domains = ['taobao.com']
    flag = 0
    page_num = 1
    comment_flag = 0

    def start_requests(self):
        """
        重写start_requests()方法，在请求中加入headers
        :return: server response
        """
        offset = 0
        while self.flag == 0:
            cookie = get_cookie()
            headers = {
                'cookie': cookie,
                'referer': get_search_api() + get_keyword()
            }

            url = get_search_api() + get_keyword() + '&s=' + str(offset)
            offset += 44
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        """
        获取商品列表，并获取每件商品的相关数据
        :param response: 商品列表
        :return: 根据产品的detail_url向服务器发出请求后服务器返回的响应数据
            item_id: 商品ID
            user_id: 商家ID
            title: 商品标题
            url: 商品评价API
        """
        try:
            data = response.css('script::text').extract()[3].split('\n')[2].strip()[16:].strip(';')
            data = json.loads(data)
            datas = data['mods']['itemlist']['data']['auctions']
            for data in datas:
                item_id = data['nid']
                user_id = data['user_id']
                title = data['raw_title']
                url = 'https:' + data['detail_url']
                page = 1
                while self.comment_flag == 0:
                    cookie = get_cookie()
                    headers = {
                        'cookie': cookie,
                        'referer': url
                    }
                    comment_url = get_comment_api() + item_id + '&sellerId=' + user_id + '&currentPage=' + str(page)
                    page += 1
                    yield scrapy.Request(comment_url, headers=headers, meta={'title': title, 'page': page - 1}, callback=self.parse_comment, dont_filter=True)
                    time.sleep(random.randint(1, 5))
            self.page_num += 1
        except json.decoder.JSONDecodeError:
            self.flag = 1

    def parse_comment(self, response):
        """
        获取商品评论
        :param response: 商品评论
        :return: item（把获取到的数据传到scrapy的items中，由scrapy的pipelines进行处理）
        """
        item = TaobaoItem()
        try:
            data = response.text.split('(')
            data1 = ''
            for num in range(1, len(data)):
                data1 += data[num]
            data = data1.strip(')')
            data = json.loads(data)
            datas = data['rateDetail']['rateList']
            for data in datas:
                rate_content = data['rateContent']
                rate_date = data['rateDate']
                print('评价内容：%s  评价时间：%s' % (rate_content, rate_date))
                item['rate_content'] = rate_content
                item['rate_date'] = rate_date
                yield item
        except json.decoder.JSONDecodeError:
            print('滑动验证出现了')
            print('解决方案：\n1、设置代理IP池，使用随机IP访问\n2、设置cookie池，使用随机cookie访问\n3、打开浏览器滑动一下重新复制并替换cookie')
