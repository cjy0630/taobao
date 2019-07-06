# -*- coding: utf-8 -*-
import os

import pymysql

from taobao.config.config_operate import get_db_settings


def removal(value):
    db_settings = get_db_settings()
    conn = pymysql.connect(host=db_settings[0], port=db_settings[1], user=db_settings[2], passwd=db_settings[3],
                           db=db_settings[4], charset='utf8')
    cur = conn.cursor()
    select_sql = 'SELECT * FROM taobao.grab_records where grab_id = "' + value + '"'
    try:
        result = cur.execute(select_sql)
        return result
    except:
        print("Select is failed")


if __name__ == '__main__':
    removal('15191a3a4d3daec53c87c835cc142898')
