# -*- coding: utf-8 -*-
def input_validation(user_ipt):
    """
    用于验证用户的输入如果输入的是数字则返回True，如果输入的不是数字则返回False
    :param user_ipt: 用户输入的字符
    :return: True or False
    """
    try:
        int(user_ipt)
        return True
    except ValueError:
        return False
