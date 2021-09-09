# 定义一个common的类，它的父类是object
import requests

class Common(object):
    # common的构造函数
    def __init__(self, url_root):
        # 被测系统的根路由
        self.url_root = url_root

    # 封装自己的get请求
    def get(self, uri, params=''):
        # 拼凑访问的地址
        url = self.url_root + uri + params
        # 通过get请求访问对应地址
        res = requests.get(url)
        return res

    def post(self, uri, params=''):
        # 拼凑访问地址
        url = self.url_root + uri
        if len(params) > 0:
            # 如果有参数，那么通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url)
        return res


