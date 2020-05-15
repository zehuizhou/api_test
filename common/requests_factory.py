#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 13:25
# @Author : zhouzehui
import requests
import configparser
import os
from common.logger import log

#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#
session = requests.session()


def requests_factory(method='post', path=None, ids=None, **kwargs):
    """
    加工request请求，传入基础配置
    :param path: 相对路径
    :param method: post、put、delete、update
    :param ids: 元组类型，处理resultful接口url中的id，例如：10.10.201.223:4001/user-service/supervisors/1/users
    :param kwargs: 传入字典，例如：data、json、params、headers
    :return: requests返回的dict
    """
    conf = configparser.ConfigParser()
    conf.read(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/conf.ini", encoding="utf-8")

    env = conf["cmd"]["env"]
    host = conf[env]["server_host"]
    user_id = conf["user"]["user_id"]

    if '{}' in path or isinstance(ids, tuple):
        path = path.format(*ids)

    headers = {
        "companyId": str(1),
        "userId": str(user_id),
        "Content-Type": "application/json"
    }
    if not kwargs.get("headers"):
        kwargs.update(headers=headers)

    if 'http' in path:
        requests_url = path
    else:
        requests_url = host + path
    result = session.request(method, requests_url, **kwargs)
    log.info(f'【请求地址】:{requests_url} 【请求方法】:{method} 【请求参数】:{kwargs}')
    log.info(f'【返回结果】:{result.json()}')
    return result.json()
