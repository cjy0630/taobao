# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi

from taobao.items import GrabRecordsItem, TaobaoItem
from taobao.unit.removal import removal_comment


class TaobaoPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        # 获取settings文件中的数据库设置
        dbparms = {
            'host': settings['MYSQL_HOST'],
            'port': settings['MYSQL_PORT'],
            'db': settings['MYSQL_DBNAME'],
            'user': settings['MYSQL_USER'],
            'passwd': settings['MYSQL_PASSWORD'],
            'charset': 'utf8mb4',
            'use_unicode': True,
        }
        # 使用twisted的adbapi函数连接数据库
        dbpool = adbapi.ConnectionPool('pymysql', **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        if isinstance(item, GrabRecordsItem):
            # 调用do_insert函数将item中的数据存入数据库
            query = self.dbpool.runInteraction(self.do_insert_grab_records, item)
            query.addErrback(self.handle_error, item, spider)
        elif isinstance(item, TaobaoItem):
            # 调用do_insert函数将item中的数据存入数据库
            if removal_comment(item['comment_id']) == 0:
                query = self.dbpool.runInteraction(self.do_insert_to_comment, item)
                query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        # 打印错误信息
        print(failure)

    def do_insert_grab_records(self, cursor, item):
        # 从item中获取sql语句
        insert_sql, params = item.get_insert_sql_grab()
        # 执行数据库操作
        cursor.execute(insert_sql, params)

    def do_insert_to_comment(self, cursor, item):
        # 从item中获取sql语句
        insert_sql, params = item.get_insert_sql()
        # 执行数据库操作
        cursor.execute(insert_sql, params)
