#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/5 10:19
# @Author : zhouzehui
from common import fake_data
import random

login_data = {
    "mobile": None,
    "password": None,
    "device": "fdfddd",
    "ip": "10.10.20.20",
    "os": "web",
    "imei": "fjidjihhidsf"
}

customer_data = {
    "userName": fake_data.fake_name_female,
    "customerLevelId": 1,
    "customerSourceId": 1,
    "companyName": fake_data.fake_name_female + '集团',
    "provinceName": "浙江省",
    "cityName": "杭州市",
    "districtName": "江干区",
    "address": fake_data.fake.address(),
    "customerIndustryId": 2,
    "customerIndustryAnnualValueId": 2,
    "name": "wen",
    "customerContactTypeId": 2,
    "mobile": "18258554212",
    "description": "联系人备注",
    "position": "Java开发工程",
    "customerIndustryTypeId": 2,
    "customerIndustryScaleId": 2,
    "majorBusiness": "主营业务",
    "profitability": "赢利能力",
    "remark": "备注"
}

checkin_data = {"companyName": "唐龙果蔬dfsdfdf````",
                "address": "顺福路20号附近dfdfdsf223@!`",
                "checkinLongitude": 120.210364,
                "checkinLatitude": 30.254622,
                "companyLongitude": 120.210364,
                "companyLatitude": 30.254622,
                "remarks": "dsfsdfsdfdsfdsf",
                "imei": "123456789",
                "phoneName": "",
                "isForce": 0,
                "files": [{
                    'data': '/9j/4AAQSkZJRgABAQAASABIAAD/4QBYRXhpZgAATU0AKgAAAAgAAgESAAMAAAABAAEAAIdpAAQAAAABAAAAJgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAB9KADAAQAAAABAAABTQAAAAD/7QA4UGhvdG9zaG9w',
                    'fileSize': 291283,
                    'name': 'IMG_0003.JPG',
                    'type': 'multipart/form-data',
                    'uri': 'file:///Users/alman/Library/Developer/CoreSimulator/Devices/82BB8CAD-634D-4A6C-9895-DA8593A4E65D/data/Containers/Data/Application/4AC2E0DF-8B0F-4B18-B4B9-06FC6329D130/Documents/055A7AD3-3F08-405C-942E-1EE6D1CAABA2.jpg'
                }]}

schedule_data = {
    'userId': None,
    'customerId': None,
    'gmtVisit': '2022-09-06 16:10:12',
    'companyName': '公司名称',
    'visitPolicy': '拜访策略123qwe~'
}

update_schedule_data = {
    'userId': None,
    'customerId': None,
    'gmtVisit': '2030-09-06 08:10:12',
    'companyName': '公司名称',
    'visitPolicy': '拜访策略修改后的123qwe~'
}

visit_data = {
    "userId": 1,
    "userIds": [1],
    "customerId": None,
    "gmtContact": "2019-05-02 12:00",
    "visitTypeId": random.randint(1, 2),
    "customerLevelId": 2,
    "customerRequirementIds": [1, 2],
    "customerObjectionIds": [2, 3],
    "customerRequirementRemark": "~~~123哈哈哈军或军",
    "visitRemark": "~~~123fgdgrebvbv",
    "objectionRemark": "~~~哈哈哈fgfdgd",
    "gmtVisit": "2019-05-01 12:02",
    "policy": "下次拜访策略呀"
}

sign_data = {
    "customerId": None,
    "productId": 1,
    "gmtSignOrder": "2019-07-01 13:23:33",
    "signAmount": 60000.12
}

receives_plan_data = {
    "customerId": None,
    "customerSignOrderId": None,
    "gmtPlanReceive": "2029-10-01 10:00:00",
    "planReceiveAmount": "123123"
}

receives_real_data = {
    "id": None,
    "gmtRealityReceive": "2019-10-01 11:00:00",
    "realityReceiveAmount": "1231213"
}
# 分配
allocations_data = {
    "newUserId": 2,
    "type": 1,
    "customerDTOS": [
        {
            "customerId": None,
            "customerName": "调配客户名称",
            "levelId": 5,
            "colorValue": "#5CBA00",
            "levelName": "2类",
            "oldUserId": None,
            "oldUserName": "危向荣"
        }
    ]
}
# 调配
deploy_data = {
    "newUserId": 3,
    "type": 0,
    "customerDTOS": [
        {
            "customerId": None,
            "customerName": "公司1客户2",
            "levelId": 5,
            "colorValue": "#5CBA00",
            "levelName": "2类",
            "oldUserId": 2,
            "oldUserName": "危向荣"
        }
    ]
}
# 移除公海
in_sea_data = {
    "customerId": None,
    "turnType": 0,
    "customerMoveReasonId": 1,
    "remark": "测试移出公海"
}

# 日报
report_data = {
    "content": "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "userId": None,
    "activityIdList": None
}

# 推送
push_data = {
    "type": 1,
    "title": "测试标题",
    "content": "测试内容"
}
