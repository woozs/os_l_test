#!/usr/bin/env.ini python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 11:06
# @Author  : mrwuzs
# @Site    : 
# @File    : test_network.py
# @Software: PyCharm



import allure
import pytest


from Params.params import Network
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestProject:

    @allure.feature('network')
    @allure.severity('blocker')
    @allure.story('Create_Network')
    def test_crete_network(self):
        """
            用例描述：创建网络
        """
        conf = Config()
        data = Network()
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
        assert test.assert_in_text(response['body'], 'auto_api_netwrok')
        Consts.RESULT_LIST.append('True')
        network_id = response["body"]["network"]["id"]
        #network，作为全局变量写入配置文件
        conf.set_conf("test_data","network_id",network_id)




if __name__ == "__main__":
    pytest.main(["-s", "test_project.py"])