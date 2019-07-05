# -*- coding: utf-8 -*-
from configparser import RawConfigParser


def get_cookie():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    section = rcp.sections()[0]
    cookie = rcp.items(section)[0][1]
    return cookie


def set_cookie(new_cookie):
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    rcp.set('my_settings', 'cookie', new_cookie)
    with open('taobao/config/settings.cfg', 'w') as f:
        rcp.write(f)


def set_search_api(new_search_api):
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    rcp.set('my_settings', 'search_api', new_search_api)
    with open('taobao/config/settings.cfg', 'w') as f:
        rcp.write(f)


def get_search_api():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    section = rcp.sections()[0]
    search_api = rcp.items(section)[2][1]
    return search_api


def set_keyword(new_keyword):
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    rcp.set('my_settings', 'keyword', new_keyword)
    with open('taobao/config/settings.cfg', 'w') as f:
        rcp.write(f)


def get_keyword():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    section = rcp.sections()[0]
    search_api = rcp.items(section)[1][1]
    return search_api


def set_comment_api(new_comment_api):
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    rcp.set('my_settings', 'comment_api', new_comment_api)
    with open('taobao/config/settings.cfg', 'w') as f:
        rcp.write(f)


def get_comment_api():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    section = rcp.sections()[0]
    comment_api = rcp.items(section)[3][1]
    return comment_api


def get_now_settings():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    section = rcp.sections()[0]

    for item in rcp.items(section):
        print(item[0] + '：' + item[1])


def set_crawl_page(new_crawl_page):
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    rcp.set('my_settings', 'crawl_page', new_crawl_page)
    with open('taobao/config/settings.cfg', 'w') as f:
        rcp.write(f)


def get_crawl_page():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    section = rcp.sections()[0]
    crawl_page = int(rcp.items(section)[4][1])
    return crawl_page


def set_comment_page(new_comment_page):
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    rcp.set('my_settings', 'comment_page', new_comment_page)
    with open('taobao/config/settings.cfg', 'w') as f:
        rcp.write(f)


def get_comment_page():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    section = rcp.sections()[0]
    comment_page = int(rcp.items(section)[5][1])
    return comment_page


def initialization():
    rcp = RawConfigParser()
    rcp.read("taobao/config/settings.cfg")
    rcp.set('my_settings', 'cookie', '')
    rcp.set('my_settings', 'keyword', '')
    rcp.set('my_settings', 'search_api', 'https://s.taobao.com/search?q=')
    rcp.set('my_settings', 'comment_api', 'https://rate.tmall.com/list_detail_rate.htm?itemId=')
    rcp.set('my_settings', 'crawl_page', '100')
    rcp.set('my_settings', 'comment_page', '8')
    with open('taobao/config/settings.cfg', 'w') as f:
        rcp.write(f)
