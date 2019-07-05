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
    offset = 0
    count = 1
    page = 0
    comment_count = 0

    def start_requests(self):
        """
        重写start_requests()方法，在请求中加入headers
        :return: server response
        """
        cookie = get_cookie()
        headers = {
            'cookie': cookie,
            'referer': get_search_api() + get_keyword()
        }

        url = get_search_api() + get_keyword() + '&s=0'
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
                comment_url = get_comment_api() + item_id + '&sellerId=' + user_id + '&currentPage=1'
                cookie = get_cookie()
                headers = {
                    'cookie': cookie,
                    'referer': url
                }
                yield scrapy.Request(comment_url, headers=headers, meta={'referer': url, 'item_id': item_id, 'user_id': user_id, 'title': title}, callback=self.parse_comment, dont_filter=True)
            self.offset += 44
            cookie = get_cookie()
            headers = {
                'cookie': cookie,
                'referer': get_search_api() + get_keyword()
            }
            search_url = get_search_api() + get_keyword() + '&s=' + str(self.offset)
            yield scrapy.Request(search_url, headers=headers, callback=self.parse, dont_filter=True)
            self.count += 1
            time.sleep(random.randint(1, 5))
        except Exception as e:
            error = e
            print('爬取结束，共%d页商品，%d条评价' % (self.count - 1, self.comment_count))
        except json.decoder.JSONDecodeError:
            print('滑动验证出现了')
            print('解决方案：\n1、设置代理IP池，使用随机IP访问\n2、设置cookie池，使用随机cookie访问\n3、打开浏览器滑动一下重新复制并替换cookie')

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
                item_id = response.meta['item_id']
                user_id = response.meta['user_id']
                title = response.meta['title']
                rate_content = data['rateContent']
                rate_date = data['rateDate']
                print('商品ID：%s  商家ID：%s  评价内容：%s  评价时间：%s' % (item_id, user_id, rate_content, rate_date))
                item['keyword'] = get_keyword()
                item['item_id'] = item_id
                item['user_id'] = user_id
                item['title'] = title
                item['rate_content'] = rate_content
                item['rate_date'] = rate_date
                self.comment_count += 1
                yield item
            self.page += 1
            cookie = get_cookie()
            headers = {
                'cookie': cookie,
                'referer': response.meta['referer']
            }
            item_id = response.meta['item_id']
            user_id = response.meta['user_id']
            comment_url = get_comment_api() + item_id + '&sellerId=' + user_id + '&currentPage=' + str(self.page)
            yield scrapy.Request(comment_url, headers=headers, callback=self.parse_comment, dont_filter=True)
            time.sleep(random.randint(1, 5))
        except Exception as e:
            error = e
        except json.decoder.JSONDecodeError:
            print('滑动验证出现了')
            print('解决方案：\n1、设置代理IP池，使用随机IP访问\n2、设置cookie池，使用随机cookie访问\n3、打开浏览器滑动一下重新复制并替换cookie')
