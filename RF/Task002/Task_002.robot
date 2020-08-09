RobotFramework 作业 2
创建一个测试套件文件，实现 2个测试用例：
用例1：
    1.  用Python语言开发一个测试库 course_mgr.py。
        该库有一个函数 listCourse 可以返回教管系统的所有课程（可以使用requests库开发）。
    2.  用RF测试用例来使用 listCourse 关键字， 根据其返回的课程列表，
        将所有的课程名输出到日志文件中（使用循环）
        验证是否和预期课程相同
用例2：
    登录网站https://www.vmall.com/index.html
    获得所有热销单品的名称，打印在log报表中

*** Settings ***
Library  course_mgr

*** Test Cases ***
用例1
    ${courseList}=  listCourse
    FOR  ${one}  IN  @{courseList}
    LOG TO CONSOLE   ${one}
    END
    ${expected}=      Create List     小学语文
    Should Be Equal     ${courseList}     ${expected}

用例2
    OPEN BROWSER  https://www.vmall.com  chrome
    set selenium implicit wait  3
    ${name}=  Get WebElements  CSS= .fl>ul.grid-list.clearfix >li >a > .grid-title
    FOR  ${one}  IN  @{name}
    LOG TO CONSOLE   ${one.text}
    END
    CLOSE BROWSER