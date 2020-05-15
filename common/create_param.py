#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/14 9:07
# @Author : zhouzehui
import copy

def newparam(body, kv) -> dict:
    """
    改造body数据
    :param body: 传入的字典
    :param param: 修改的键值对，字典格式，如{'id': 1}
    :return:
    """
    newbody = copy.deepcopy(body)
    newbody.update(kv)
    return newbody