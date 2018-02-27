
# coding:utf-8

import requests
import json


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = ""

    def send_sms(self, code, mobile):
        params = {
            'apukey': self.api_key,
            'mobile': mobile,
            'text': "[暮雪]您的验证码是{code}，如非本人操作，请忽略本短信".format(code=code)
        }
        response = requests.post(self.single_send_url,data=params)
        re_dict = json.loads(response.text)

if __name__=="__main__":
    """
    需要将服务器IP添加到云片网白名单中。在个人账户的设置中设置
    """
    yunpian = YunPian('')
    yunpian.send_sms('2017', '12132212112')