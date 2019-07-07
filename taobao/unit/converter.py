# -*- coding: utf-8 -*-
import hashlib


def to_md5(value):
    """
    用于将字符串转换为md5
    :param value: 接收的待转字符串
    :return: 转换为md5的字符串
    """
    md5 = hashlib.md5()
    md5.update(value.encode(encoding='utf-8'))
    new_value = md5.hexdigest()
    return new_value


def to_unicode(value):
    pass
