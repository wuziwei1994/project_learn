RobotFramework 作业 4
自动化如下测试用例
用例：检查添加课程功能
前置条件：系统中没有课程，
步骤 1： 添加课程，输入课程名、详情描述、展示次序为2，点击创建
预期结果：创建的课程正确显示在下面的表中。
步骤 2： 再添加一门课程，输入课程名、详情描述、展示次序为1，点击创建
预期结果：创建的课程正确显示在下面的表中，并且按照展示次序排列。
这里为了简化，我们只检查 课程名就可以了
要求：
将用例中的 登录、添加课程、检查课程， 合理使用 资源文件里面的用户关键字  实现
如果可以，将初始化、清除操作 也改为用 用户关键字实现
*** Settings ***
Library  SeleniumLibrary
Library  Collections
Resource    rc.robot
Suite Setup    Setup OpenBrowser
Suite Teardown   TearDown CloseBrowser
*** Test Cases ***
case1
    # 初始化环境，删除所有课程
    [Setup]  Del Lessons
    # 添加课程1
    Add Lesssins    初中数学    初中数学   2
    # 添加课程2
    Add Lesssins    初中语文    初中语文   1
    # 获取实际结果
    ${lessons}=  Get LessonsName
    # 创建预期结果
    ${expected}=  create list  初中语文   初中数学
    # 断言
    Should Be True   ${lessons} == ${expected}



