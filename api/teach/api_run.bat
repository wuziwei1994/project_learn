@echo off
echo ׼����ʼ�����Զ����ű�
@echo on



del /f /s /q  D:\teach\report\tmp\*.json
del /f /s /q  D:\teach\report\tmp\*.jpg
del /f /s /q  D:\teach\report\report



@echo off
echo ɾ���������ļ�����ʼ����
@echo on


cd  D:\teach\test_CaseTeach
pytest  -sq --alluredir=../report/tmp --allure-severities=normal,critical
allure generate  ../report/tmp -o ../report/report --clean


@echo off
echo �������
pause
 
