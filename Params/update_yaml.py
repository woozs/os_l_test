#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 16:55
# @Author  : mrwuzs
# @Site    : 
# @File    : update_yaml.py
# @Software: PyCharm
#coding:utf-8
import os
import yaml

def  update_yaml(response,file):
    curpath = os.path.dirname(os.path.realpath(__file__))
    yamlpath = os.path.join(curpath+"\\Param\\", file)

    # 写入到yaml文件
    with open(yamlpath, "w", encoding="utf-8") as f:
        yaml.dump(response["body"], f)
