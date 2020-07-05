# author：xintian   
# time:2020-06-19
#-*- coding: utf-8 -*-
import pytest,json,shutil
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
@pytest.fixture(scope='module',autouse=True)#环境初始化 、数据清除
def delete_all_lesson(request):
    # try:
    #     shutil.rmtree('../report/tmp')  # 清空tmp目录下的文件
    #     shutil.rmtree('../report/report')  # 清空report目录下的文件
    # except:
    #     print('---文件路径不存在----')
    # 1- 登录
    session = LoginClass().api_login('{"username": "auto","password": "sdfsdfsdf"}')
    #2- 列出所有课程
    inData = {'action': 'list_course',
               'pagenum' :'1',
                'pagesize' : '20'
               }
    resList = json.loads(LessonClass().list_lesson(session,inData))['retlist']
    while resList !=[]:
        for one in resList:
            lessonId = one['id']#获取课程id
            # 3- 删除所有的课程
            LessonClass().delete_all_lesson(session,lessonId)
        resList = json.loads(LessonClass().list_lesson(session,inData))['retlist']
    #创建课程测试数据
    for one in range(1,7):
        lessonData = {"name": f"心田{one:0>3}", "desc": "初中化学课程", "display_idx": f"{one}"}
        LessonClass().add_lesson(session,json.dumps(lessonData))

    #环境、数据清除----teardown
    def fin():

        print('----测试环境恢复----')

    request.addfinalizer(fin)

#一个xx.py  可以有很多个class


