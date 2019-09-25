#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 22:17
# @Author  : mrwuzs
# @Site    : 
# @File    : test_project.py
# @Software: PyCharm

import allure
import pytest


from Params.params import Project
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestProject:

    @allure.feature('Project')
    @allure.severity('blocker')
    @allure.story('Create_Project')
    def test_basic_01(self):
        """
            用例描述：创建项目
        """
        conf = Config()
        data = Project()
        test = Assert.Assertions()
        request = Request.Request()

        host = conf.host
        req_url = 'http://' + host
        port = data.port
        urls = data.url
        params = data.data
        api_url = req_url +":"+ str(port[0]) + urls[0]
        response = request.post_request(api_url, params[0])
        assert test.assert_code(response['code'], 201)
        assert test.assert_in_text(response['body'], 'Automation_wuzs')
        Consts.RESULT_LIST.append('True')
        project_id = response["body"]["project"]["id"]
        #保存成功运行的project_id，作为全局变量写入配置文件
        conf.set_conf("test_data","project_id",project_id)



if __name__ == "__main__":
    pytest.main(["-s", "test_project.py"])