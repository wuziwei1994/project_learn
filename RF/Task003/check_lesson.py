# author：wuziwei   
# @time:2020-08-08 23:16
# coding:-*- utf-8 -*-

import requests

host = 'http://127.0.0.1'
username = 'auto'
password = 'sdfsdfsdf'


def login():
    """获取登录cookies"""
    path = f'{host}/api/mgr/loginReq'
    params = {'username': username, 'password': password}
    login_re = requests.post(path, data=params)
    return login_re.cookies


def get_lesson():
    """获取所有课程列表"""
    path = f'{host}/api/mgr/sq_mgr/'
    params = {'action': 'list_course', 'pagenum': '1', 'pagesize': '20'}
    get_lesson_re = requests.get(path, params=params, cookies=login())
    return get_lesson_re.json()['retlist']


def del_lesson():
    """根据课程ID，删除所有课程"""
    lesson_id = [one['id'] for one in get_lesson()]
    for one in lesson_id:
        path = f'{host}/api/mgr/sq_mgr/'
        params = {'action': 'delete_course', 'id': one}
        requests.delete(path, data=params, cookies=login())


def add_lesson():
    """添加一个课程"""
    path = f'{host}/api/mgr/sq_mgr/'
    params = {'action': 'add_course', 'data': '{"name": "初中化学", "desc": "初中化学课程", "display_idx": "4"}'}
    add_lesson_re = requests.post(path, data=params, cookies=login())
    return add_lesson_re.json()['retcode']


def assert_lesson():
    """获取课程名称列表"""
    return [one['name'] for one in get_lesson()]


if __name__ == '__main__':
    print(get_lesson())
