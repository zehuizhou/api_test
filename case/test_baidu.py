#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2020-05-15 14:20
#  @Author  : July
import pytest
import requests


# @pytest.mark.parametrize('a', '', ids='测试百度是否能正常访问')
def test_baidu():
    ret = requests.get(url='https://www.baidu.com/')
    assert ret.status_code == 200


# 待测函数
def add(a, b):
    return a + b


data = [(1, 2, 3), (4, 5, 9), ('1', '2', '12')]
ids = [f'测试数据{d}' for d in range(len(data))]  # => 生成与数据数量相同的名称列表


@pytest.mark.parametrize('a, b, c', data, ids=ids)
def test_add(a, b, c):
    print(f'\na,b,c的值:{a},{b},{c}')
    assert add(a, b) == c
