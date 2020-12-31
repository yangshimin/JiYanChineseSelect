# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 12/31/20
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : public_func.py
# @Software: PyCharm
from hashlib import md5


def get_md5(data):
    md5_ = md5()
    md5_.update(data)
    return md5_.hexdigest()
