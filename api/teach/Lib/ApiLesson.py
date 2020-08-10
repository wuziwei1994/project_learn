# author：xintian   
# time:2020-06-17
#-*- coding: utf-8 -*-
from api.teach.config  import HOST
import requests
import json
from Lib.ApiLogin import LoginClass
from Lib.GetExcelData import get_excelData
class LessonClass:
    def add_lesson(self,session,inData):
        user_cookie = {'sessionid': session}  # 自己封装
        # 1- 路径-url
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}  # 字典
        # 2- 参数
        payload = {
            'action': 'add_course',
            'data': inData#转json
        }

        reps = requests.post(api_url, data=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        return reps.text#返回值可以自行定义  assert

    # 2- 列出课程
    def list_lesson(self, session, inData):
        user_cookie = {'sessionid': session}  # 自己封装
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        payload = inData
        # print(payload)
        reps = requests.get(api_url, params=payload, cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text

    #3- 删除课程
    def delete_all_lesson(self, session, inId):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = {'action': 'delete_course',
                   'id': int(inId)
                   }
        reps = requests.delete(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text

    def delete_lesson(self, session, inData):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = inData
        reps = requests.delete(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text

    def modify_lesson(self, session, inData):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = inData
        reps = requests.put(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text