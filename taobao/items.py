# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:

    comment_id = scrapy.Field()
    keyword = scrapy.Field()
    item_id = scrapy.Field()
    user_id = scrapy.Field()
    title = scrapy.Field()
    comment_user = scrapy.Field()
    rate_content = scrapy.Field()
    rate_date = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = 'replace into comment(comment_id, keyword, item_id, user_id, title, comment_user, rate_content, rate_date) values (%s, %s, %s, %s, %s, %s, %s, %s)'
        params = (
            self['comment_id'],
            self['keyword'],
            self['item_id'],
            self['user_id'],
            self['title'],
            self['comment_user'],
            self['rate_content'],
            self['rate_date']
        )
        return insert_sql, params


class GrabRecordsItem(scrapy.Item):
    grab_id = scrapy.Field()
    title = scrapy.Field()
    grab_url = scrapy.Field()

    def get_insert_sql_grab(self):
        insert_sql = 'replace into grab_records(grab_id, title, grab_url) values (%s, %s, %s)'
        params = (
            self['grab_id'],
            self['title'],
            self['grab_url']
        )
        return insert_sql, params
