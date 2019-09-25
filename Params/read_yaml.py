#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 18:23
# @Author  : mrwuzs
# @Site    : 
# @File    : read_yaml.py
# @Software: PyCharm
import yaml
import os
# 作者：上海-悠悠 交流QQ群：588402570
# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath+"\\Param\\", "Network.yaml")
# open方法打开直接读出来
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()
print(type(cfg))  # 读出来是字符串
print(cfg)

def yaml_include(loader, node):
    # Get the path out of the yaml file
    file_name = os.path.join(os.path.dirname(loader.name), node.value)

    with open(file_name) as inputfile:
        return yaml.load(inputfile)

yaml.add_constructor("!include", yaml_include)
