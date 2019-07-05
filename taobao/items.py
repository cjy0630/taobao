# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    keyword = scrapy.Field()
    item_id = scrapy.Field()
    user_id = scrapy.Field()
    title = scrapy.Field()
    rate_content = scrapy.Field()
    rate_date = scrapy.Field()

    def get_insert_sql(self):
        # sql语句，用与向数据库中插入数据，此处我没有使用insert into，而是使用的replace into
        # replace into是向数据库中插入数据时，根据主键进行判断，如果数据已经存在则先删除掉原有数据再插入新的数据，如果数据不存在则直接进行插入
        # 由于考虑到用户可能修改评价，所以此处使用replace into进行插入，以保证所有数据都是最新的
        insert_sql = 'replace into comment(keyword, item_id, user_id, title, rate_content, rate_date) values (%s, %s, %s, %s, %s, %s)'
        params = (
            self['keyword'],
            self['item_id'],
            self['user_id'],
            self['title'],
            self['rate_content'],
            self['rate_date']
        )
        return insert_sql, params
