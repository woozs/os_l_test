#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 20:50
# @Author  : mrwuzs
# @Site    : 
# @File    : Token.py
# @Software: PyCharm

import requests

from Common import Log
from Conf import Config


class Token:
    def __init__(self):
        self.config = Config.Config()
        self.log =  Log.MyLog()

    def get_token(self):
        """
        获取token
        :return: token-id
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Content-Type": "application/json"
        }
        login_url = "http://" + self.config.host +":5000/v3/auth/tokens"
        param = self.config.loginInfo
        response = requests.post(login_url, param, headers=headers)
        return  response.headers.get("X-Subject-Token")

if __name__ == '__main__':
    token = Token()
    print(token.get_token())