#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-15 14:20
# @Author  : July
import pytest
import requests


def test_baidu():
    ret = requests.get(url='https://www.baidu.com/')
    assert ret.status_code == 200
