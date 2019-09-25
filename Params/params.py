#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 9:10
# @Author  : mrwuzs
# @Site    : 
# @File    : params.py
# @Software: PyCharm
"""
定义所有测试数据

"""
import os

from Params import tools
from Common import Log
from Common import VarsubYaml
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param

class Project:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Project.yaml')
    params = get_parameter('Poject')
    url = []
    data = []
    port = []

    for i in range(0, len(params)):
        url.append(params[i]['url'])
        port.append(params[i]['port'])
        data.append(params[i]['data'])



class Network:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Network.yaml')
    params = get_parameter('Network')
    url = []
    data = []
    port = []


    for i in range(0, len(params)):
        url.append(params[i]['url'])
        port.append(params[i]['port'])
        data.append(params[i]['data'])


