# -*- coding: utf-8 -*-
# @Author: nickel
# @File:test_baidu.py
# @Time: 2021/11/7 10:47
import requests

from read_testcase import read_testcase
from write_testresult import write_result


def test_baidu():
    #  读取测试用例，获取接口信息
    interface_list = read_testcase()
    # 测试结果
    test_result = []
    # 循环执行接口测试
    for i in interface_list:
        r = requests.request(method=i[0], url=i[1])
        print(r.text)
        try:
            assert i[2] in r.text
            test_result.append("pass")
        except:
            test_result.append("fail")
    print(test_result)

    # 回写测试结果
    write_result(test_result)