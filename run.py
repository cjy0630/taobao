# -*- coding: utf-8 -*-
from scrapy import cmdline

from taobao.config.config_operate import set_cookie, set_search_api, set_keyword, set_comment_api, get_now_settings, \
    set_crawl_page, set_comment_page, initialization
from taobao.unit.input_validation import input_validation
from taobao.unit.show_info import show_info


def user_input(ipt_type):
    """
    用于接收用户输入并进行验证
    :return: 用户输入的编号
    """
    if ipt_type == 'menu':
        ipt = input('请输入号码选择要进行的操作：')
        if input_validation(ipt):
            return ipt
        else:
            user_input('menu')
    elif ipt_type == 'crawl_page':
        ipt = input('请输入获取商品页数：')
        if input_validation(ipt):
            return ipt
        else:
            user_input('crawl_page')
    elif ipt_type == 'comment_page':
        ipt = input('请输入获取评价页数：')
        if input_validation(ipt):
            return ipt
        else:
            user_input('comment_page')


if __name__ == '__main__':
    show_info()

    while True:
        user_ipt = user_input('menu')
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
        elif user_ipt == '6':
            ipt = user_input('crawl_page')
            set_crawl_page(ipt)
            ipt = user_input('comment_page')
            set_comment_page(ipt)
        elif user_ipt == '7':
            initialization()
