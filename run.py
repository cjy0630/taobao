# -*- coding: utf-8 -*-
from scrapy import cmdline

from taobao.config.config_operate import set_cookie, set_search_api, set_keyword, set_comment_api, get_now_settings
from taobao.unit.input_validation import input_validation
from taobao.unit.show_info import show_info


def user_input():
    """
    用于接收用户输入并进行验证
    :return: 用户输入的编号
    """
    ipt = input('请输入号码选择要进行的操作：')
    if input_validation(ipt):
        return ipt
    else:
        user_input()


if __name__ == '__main__':
    show_info()

    while True:
        user_ipt = user_input()
        if user_ipt == '1':
            ipt = input('请输入要搜索的商品：')
            set_keyword(ipt)
            print('正在获取商品及评价，请耐心等待...')
            # cmdline.execute('scrapy crawl alcohol'.split())
            cmdline.execute('scrapy crawl alcohol -s LOG_FILE=all.log'.split())
        elif user_ipt == '2':
            get_now_settings()
        elif user_ipt == '3':
            ipt = input('请输入Cookie：')
            set_cookie(ipt)
        elif user_ipt == '4':
            ipt = input('请输入API：')
            set_search_api(ipt)
        elif user_ipt == '5':
            ipt = input('请输入API：')
            set_comment_api(ipt)
