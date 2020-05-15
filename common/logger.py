#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import logging
import datetime
import os
import traceback
# log_path是存放日志的路径
import sys

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'log')

# 如果不存在这个logs文件夹，就自动创建一个
os.mkdir(log_path) if not os.path.exists(log_path) else False

# 当前的毫秒级时间戳
today = datetime.date.today()

call_module = sys._getframe(6).f_code.co_filename
# call_module = traceback.extract_stack()

# 设置日志基本信息
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# 将日志信息放置在logs目录下
module_log_path = os.path.join(log_path, f'{os.path.basename(call_module)}{today}.log')
total_log_path = os.path.join(log_path, f'{today}.log')

# 设置打印和存放的日志句柄
fileHandler = logging.FileHandler(module_log_path, encoding='utf-8')
consoleHandler = logging.StreamHandler()
totalHandler = logging.FileHandler(total_log_path, encoding="utf-8")

# 设置日志格式
FileFormat = "[%(asctime)s]-[%(levelname)s]-[%(module)s]-[%(funcName)s]-[%(lineno)d]:%(message)s"
# ConsoleFormat = "[%(asctime)s]-[%(levelname)s]-[%(lineno)d]:%(message)s"
ConsoleFormat = "[%(asctime)s]-[%(levelname)s]:%(message)s"
file_formatter = logging.Formatter(FileFormat)
console_formatter = logging.Formatter(ConsoleFormat)
total_formatter = logging.Formatter(FileFormat)
fileHandler.setFormatter(file_formatter)
consoleHandler.setFormatter(console_formatter)
totalHandler.setFormatter(total_formatter)

# 添加句柄
log.addHandler(fileHandler)
log.addHandler(consoleHandler)
log.addHandler(totalHandler)
