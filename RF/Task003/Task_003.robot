# author：wuziwei   
# @time:2020-08-08 23:14
# coding:-*- utf-8 -*-

'''
创建一个RF测试套件，包含下面的一个用例
用例名：
验证当系统中没有课程的时候，是否能成功添加一个课程
前置条件：
系统中没有课程
测试步骤：
添加课程，输入课程名、详情描述、展示次序，点击创建
预期结果：
创建的课程正确显示在下面的课程列表中。
这里为了简化，我们只检查 课程名就可以了
'''

*** Settings ***
Library  check_lesson.py

*** Test Cases ***
case1
    # 初始化环境，删除所有课程
    [Setup]    del_lesson
    log to console  课程清除成功
    # 使用接口添加课程
    add_lesson
    # 创建预期结果
    ${lesson_name}=  create list  初中化学
    # 获取实际结果
    ${expected}=  assert_lesson
    # 断言
    should be true  ${lesson_name} == ${expected}

