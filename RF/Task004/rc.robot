*** Settings ***
Library  SeleniumLibrary
Library    Collections
*** Keywords ***
Setup OpenBrowser
    open browser  http://localhost/mgr/login/login.html  chrome
    set selenium implicit wait  3

TearDown CloseBrowser
    close browser

Login Web
    go to  http://localhost/mgr/login/login.html
    input text  css=[id=username]   auto
    input text  css=[id=password]   sdfsdfsdf
    click element  css=.btn-success

Del Lessons
    Login Web
    FOR  ${one}  IN RANGE  999
    ${lessons}=  get webelements  css=button.ng-scope:nth-child(2)
    exit for loop if  $lessons==[]
    click element  @{lessons}[0]
    ${del_icon}=  get webelement    css=.btn-primary
    click element  ${del_icon}
    sleep   1
    END

Add Lesssins
    [Arguments]  ${name}    ${desc}    ${displayidx}
    Login Web
    ${new_lesson}=  get webelement  css=.glyphicon-plus
    click element  ${new_lesson}
    ${add_lesson}=  get webelement  css=[ng-model="addData.name"]
    ${add_desc}=  get webelement  css=[ng-model="addData.desc"]
    ${add_idx}=  get webelement  css=[ng-model="addData.display_idx"]
    ${add_button}=  get webelement  css=[ng-click="addOne()"]

    input text  ${add_lesson}   ${name}
    input text  ${add_desc}     ${desc}
    clear element text  ${add_idx}
    input text  ${add_idx}  ${displayidx}
    click element  ${add_button}
    sleep  2

Get LessonsName
    Login Web
    ${lessons_list}=  create list
    ${lessons_name}=  get webelements  css=tbody [style="text-align:center"]:nth-child(2)
    FOR  ${one}  IN  @{lessons_name}
    Append To List   ${lessons_list}    ${one.text}
    END
    log to console  ${lessons_list}
    [Return]   ${lessons_list}

