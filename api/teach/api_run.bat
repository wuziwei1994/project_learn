@echo off
echo 准备开始运行自动化脚本
@echo on



del /f /s /q  D:\project_learn\api\teach\report\tmp\*.json
del /f /s /q  D:\project_learn\api\teach\report\tmp\*.jpg
del /f /s /q  D:\project_learn\api\teach\report\report



@echo off
echo 删除工作区文件，开始运行
@echo on


cd  D:\project_learn\api\teach\test_CaseTeach
pytest  -sq --alluredir=../report/tmp --allure-severities=normal,critical
allure generate  ../report/tmp -o ../report/report --clean


@echo off
echo 运行完成
pause
 
