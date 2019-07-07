# -*- coding: utf-8 -*-

from taobao.unit.converter import to_md5
from taobao.unit.spiders_factory import create_spider


def get_keyword(value):
    """
    用于分割多个商品，调用spiders_factory以商品名称创建爬虫
    :param value: 输入的多个商品
    :return: not return
    """
    if value != '' and value.split('-') != ' ':
        keywords = value.split('-')
        for keyword in keywords:
            spider_name = 'c_' + to_md5(keyword)
            create_spider(spider_name, keyword)
