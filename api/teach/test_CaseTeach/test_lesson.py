# author：xintian   
# time:2020-06-17
#-*- coding: utf-8 -*-
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
import json,os
import pytest
import allure
from Lib.GetExcelData import get_excelData
@allure.feature('课程模块')#一级标题
@allure.severity("normal")
@pytest.mark.Lesson(order = 2)#标签-
class TestLesson:#测试用例类
    # 这个课程功能模块，每一个接口需要登录
    def setup_class(self):#登录
        """课程模块-登录初始化"""
        self.session = LoginClass().api_login('{"username": "auto","password": "sdfsdfsdf"}')
    # 1- 新增课程接口
    #fixtrue---参数化---excel
    @allure.story("新增课程")
    @allure.title("新增课程用例")
    @pytest.mark.lesson_add#标签--
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 2, 26, 6, 8))
    def test_add_lesson(self,inData,repsData):
        """新增课程"""
        res = LessonClass().add_lesson(self.session,inData)
        assert  json.loads(res)['retcode'] ==  json.loads(repsData)['retcode']#断言

    @allure.story("列出课程")
    @allure.title("列出课程用例")
    @pytest.mark.lesson_list
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 27, 38, 6, 8))
    def test_list_lesson(self,inData,repsData):
        """列出课程"""
        res = LessonClass().list_lesson(self.session,json.loads(inData))
        assert  json.loads(res)['retcode'] == json.loads(repsData)['retcode']#断言

    @allure.story("删除课程")
    @allure.title("删除课程用例")
    @pytest.mark.lesson_delete
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 39, 46, 6, 8))
    def test_delete_lesson(self,inData,repsData):
        """删除课程"""
        res = LessonClass().delete_lesson(self.session,json.loads(inData))
        assert  json.loads(res)['retcode'] == json.loads(repsData)['retcode']#断言



    # @pytest.mark.modfiy_lesson
    # @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 47, 49, 6, 8))
    # def test_modify_lesson(self,inData,repsData):
    #      """修改课程"""
    #         pass



if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /tmp 目录
    pytest.main(['test_lesson.py','-s','--alluredir', '../report/tmp'])
    # 执行命令 allure generate ./tmp -o ./report --clean ，生成测试报告
    os.system('allure generate  ../report/tmp -o ../report/report --clean')


# test_add_lesson()