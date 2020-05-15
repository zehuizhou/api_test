#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 10:24
# @Author : zhouzehui

"""
user-service
"""
user_port = ":4001"
# 登录 post
authorizations_path = user_port + "/user-service/authorizations"
# 获取下属信息
supervisors_path = user_port + "/user-service/supervisors/{}/users"
# 添加员工
add_user_path = ":4001/user-service/users"
# 离职员工
leave_user_path = ":4001/user-service/users/{}/leave"
# 设置员工权限
user_modules_path = ":4001/user-service/user_modules"

"""
research-service
"""
research_port = ":4011"
# 提交回答选项 post
answers_path = research_port + "/research-service/researches/answers"
# 提交填写人 post
exams_name_path = research_port + "/research-service/researches/exams/name"
# 查询班次和差异结果 get
diffs_path = research_port + "/research-service/researches/diffs"
# 1.查询考试详情 get 2.提交该批次的考试 put
exams_path = research_port + "/research-service/researches/exams/{}"
# 查询该批次的考试列表 get
batches_exams_path = research_port + "/research-service/researches/batches/exams"
# 完成调研 put
batches_path = research_port + "/research-service/researches/batches/{}"

"""
customer-service
"""
# 客户
customer_path = ":4003/customer-service/customers"
# 联系
visit_path = ":4003/customer-service/customers/visits"
# 补充沟通记录
communicate_path = ":4003/customer-service/communicate"
communicate_detail_path = ":4003/customer-service/communicate/{}"
# 客户等级
customer_level_path = ":4003/customer-service/customers/{}/levels"
# 签单
sign_path = ":4003/customer-service/customers/signs"
# 添加回款计划
receives_plan_path = ":4003/customer-service/receives"
# 添加实际回款
receives_real_path = ":4003/customer-service/receives/records"
# 客户调配/分配
allocations_path = ":4003/customer-service/allocations"
# 移入公海
customers_in_sea_path = ":4003/customer-service/sea/customers_out_reports"
# 公海捡客户
pick_sea_customer_path = ":4003/customer-service/sea/customers_in_reports/{}"
# 客户主页接口
customer_work_flow_path = ":4003/customer-service/customers/work_flow"

"""
checkin-service
"""
checkin_path = ":4006/checkin-service/checkins"
checkin_detail_path = ":4006/checkin-service/checkins/{}"
checkin_list_path = ":4006/checkin-service/checkins"
checkin_invalid_stats = ":4006/checkin-service/checkins/invalid_stats"

"""
schedule-service
"""
schedule_path = ":4005/schedule-service/schedules"
schedule_detail_path = ":4005/schedule-service/schedules/{}"
schedule_dates_path = ":4005/schedule-service/schedules/dates"

"""
report-service
"""
report_path = ":4004/report-service/daily_reports"
report_activity_ids_path = ":4004/report-service/daily_reports/{}/activityIds"
# 获取最大已消费的日报动态id
report_activity_maxid_path = ":4004/report-service/daily_report_activity_max_id"

"""
attendance-service
"""
attendance_rules_path = ":4007/attendance-service/attendance_rules"
"""
message-service
"""
push_path = ":4009/message-service/message/messages"




"""将path添加到数组，注意，除了路径，其他属性别命名path"""
api_list = []
for i in dir():
    if 'path' in i:
        api_list.append(i)

api = [eval(i) for i in api_list]


def func(x):
    if '{}' in x:
        return x.replace('{}', '1')
    else:
        return x


url = list(map(func, api))
