# author：wuziwei   
# @time:2020-08-08 19:49
# coding:-*- utf-8 -*-
import requests


def login():
    login_url = 'http://localhost/api/mgr/loginReq'
    body = {
        'username': 'auto',
        'password': 'sdfsdfsdf'
    }
    login_re = requests.post(login_url, data=body)
    return login_re.cookies


def listCourse():
    course_url = 'http://localhost/api/mgr/sq_mgr/'
    body = {
        'action': 'list_course',
        'pagenum': 1,
        'pagesize': 20
    }
    get_course = requests.get(course_url, params=body, cookies=login())
    get_course.encoding = 'unicode_escape'
    return [one['name'] for one in get_course.json()['retlist']]


if __name__ == '__main__':
    print(listCourse())
