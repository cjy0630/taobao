# -*- coding: utf-8 -*-
import os

import pymysql

from taobao.config.config_operate import get_db_settings


def removal_grab_records(value):
    """
    用于评价页面url去重，根据评价页面url进行去重
    :param value: 接收待比对的评价页面url
    :return: 待抓取的评价页面url是否已存在（0是不存在，1是已存在）
    """
    db_settings = get_db_settings()
    conn = pymysql.connect(host=db_settings[0], port=db_settings[1], user=db_settings[2], passwd=db_settings[3],
                           db=db_settings[4], charset='utf8')
    cur = conn.cursor()
    select_sql = 'SELECT * FROM taobao.grab_records where grab_id = "' + value + '"'
    try:
        result = cur.execute(select_sql)
        if result == 0:
            print('%s不存在' % value)
        elif result == 1:
            print('%s已存在' % value)
        return result
    except:
        print("Select is failed")


def removal_comment(value):
    """
    用于写入数据库时的评价去重，根据评价信息进行去重
    :param value: 接收待比对的评价
    :return: 待入库的评价信息是否已存在（0是不存在，1是已存在）
    """
    db_settings = get_db_settings()
    conn = pymysql.connect(host=db_settings[0], port=db_settings[1], user=db_settings[2], passwd=db_settings[3],
                           db=db_settings[4], charset='utf8')
    cur = conn.cursor()
    select_sql = 'SELECT * FROM taobao.comment where comment_id = "' + value + '"'
    try:
        result = cur.execute(select_sql)
        # if result == 0:
        #     print('%s不存在' % value)
        # elif result == 1:
        #     print('%s已存在' % value)
        return result
    except:
        print("Select is failed")
