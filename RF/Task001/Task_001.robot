# author：wuziwei   
# @time:2020-08-07 22:30
# coding:-*- utf-8 -*-

*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
百度搜索松勤
    Open Browser                  http://www.baidu.com    chrome
    Set Selenium Implicit Wait    5
    Input Text                    id=kw                   松勤\n
    ${firstRet}=                  Get Text                id=1
    Should Contain                ${firstRet}             松勤网
    close browser