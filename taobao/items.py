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
        insert_sql = 'insert into comment(keyword, item_id, user_id, title, rate_content, rate_date) values (%s, %s, %s, %s, %s, %s)'
        params = (
            self['keyword'],
            self['item_id'],
            self['user_id'],
            self['title'],
            self['rate_content'],
            self['rate_date']
        )
        return insert_sql, params
