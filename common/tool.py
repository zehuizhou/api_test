#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/23 14:39
# @Author : zhouzehui
import configparser
import random

from common.requests_factory import requests_factory
from common import common_data, api_path
from common import fake_data
from common.logger import log
import os

ini_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/conf.ini"
conf = configparser.ConfigParser()
conf.read(ini_path + "/config/conf.ini", encoding="utf-8")

def add_communication():
    log.info("------开始测试，初始化用户数据------")

    user_data = {
        "existUserId": 0,
        "name": "用户" + fake_data.fake.name(),
        "mobile": "18" + str(random.randint(100000000, 999999999)),
        "gender": 1,
        "birthday": "2016-07-01",
        "attendanceGroupId": 1,
        "departments": [
            {
                "id": 6,
                "position": "设计",
                "isSupervisor": 0
            }
        ],
        "templateIds": [1]
    }

    supervisor_data = {
        "existUserId": 0,
        "name": "主管" + fake_data.fake.name(),
        "mobile": "18" + str(random.randint(100000000, 999999999)),
        "gender": 1,
        "birthday": "2015-07-01",
        "attendanceGroupId": 1,
        "departments": [
            {
                "id": 6,
                "position": "设计总监",
                "isSupervisor": 1
            }
        ],
        "templateIds": [1]
    }

    headers = {
        "companyId": str(1),
        "userId": str(1),
        "Content-Type": "application/json"
    }
    user_id = requests_factory(path=api_path.add_user_path, json=user_data, headers=headers)['data']['id']
    supervisor_id = requests_factory(path=api_path.add_user_path, json=supervisor_data, headers=headers)['data']['id']
    conf.read(ini_path)
    conf.set("user", "user_id", str(user_id))
    conf.set("user", "supervisor_id", str(supervisor_id))
    conf.write(open(ini_path, "r+", encoding="utf-8"))

    # 配置这两个用户的权限
    requests_factory(method='put', path=api_path.user_modules_path, headers=headers, json={
        "userId": user_id,
        "moduleCodes": ["crm", "admin"]
    })
    requests_factory(method='put', path=api_path.user_modules_path, headers=headers, json={
        "userId": supervisor_id,
        "moduleCodes": ["crm", "admin"]
    })

    user_id = conf["user"]["user_id"]

    log.info(f'step1------>添加客户')
    common_data.customer_data.update({"companyName": fake_data.fake.name() + fake_data.fake_name_female + '集团'})
    customer_id = requests_factory(path=api_path.customer_path, json=common_data.customer_data)['data']['id']

    log.info(f'step2------>给客户{customer_id}添加日程')
    common_data.schedule_data.update({"customerId": customer_id, "userId": user_id})
    schedule_id = requests_factory(path=api_path.schedule_path, json=common_data.schedule_data)['data']['id']

    log.info(f'step3------>修改日程{schedule_id}')
    common_data.schedule_data.update({"id": schedule_id})
    schedule_id = requests_factory(method='put', path=api_path.schedule_path, json=common_data.schedule_data)['data']['id']

    log.info(f'step4------>给客户{customer_id}添加联系,并关联日程{schedule_id+1}')
    common_data.visit_data.update({"customerId": customer_id, "scheduleId": schedule_id + 1})
    visit_id = requests_factory(path=api_path.visit_path, json=common_data.visit_data)['data']['id']

    log.info(f'step5------>给联系{visit_id}补充沟通记录')
    body = {'visitId': visit_id, 'content': '这次的沟通记录补充一下，客户需求不明确'}
    requests_factory(path=api_path.communicate_path, json=body)


    log.info(f'step6------>将客户{customer_id}移到公海')
    headers = {
        "companyId": str(1),
        "userId": user_id,
        "Content-Type": "application/json"
    }
    common_data.in_sea_data.update({"customerId": customer_id})
    requests_factory(path=api_path.customers_in_sea_path, json=common_data.in_sea_data, headers=headers)


    log.info(f'step7------>添加客户')
    common_data.customer_data.update({"companyName": fake_data.fake.name() + fake_data.fake_name_female + '集团'})
    customer_id = requests_factory(path=api_path.customer_path, json=common_data.customer_data)['data']['id']

    log.info(f'step8------>给客户{customer_id}添加日程')
    common_data.schedule_data.update({"customerId": customer_id, "userId": user_id})
    requests_factory(path=api_path.schedule_path, json=common_data.schedule_data)

    log.info(f'step3------>给客户{customer_id}添加签到')
    common_data.checkin_data.update({"customerId": customer_id})
    requests_factory(method='post', path=api_path.checkin_path, json=common_data.checkin_data)


a = [1, 2, 3, 4, 5, 6]
print(a[0:2])
