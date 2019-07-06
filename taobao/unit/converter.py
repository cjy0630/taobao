# -*- coding: utf-8 -*-
import hashlib


def to_md5(value):
    md5 = hashlib.md5()
    md5.update(value.encode(encoding='utf-8'))
    new_value = md5.hexdigest()
    return new_value


def to_unicode(value):
    pass
