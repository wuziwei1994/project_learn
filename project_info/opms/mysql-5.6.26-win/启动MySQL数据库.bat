@echo off
title MySQL v_5_6_26---���ڽ���������֪��Ʒ�� Ctrl+C����������
@echo ��������MySQL...
@echo .
@echo ...С��ʾ..................................................................
@echo .                                                                         .
@echo . MySQLĬ�ϲ���                                                           .
@echo . ������/IP��127.0.0.1                                                    .
@echo . �û�����root                                                            .
@echo . ���룺123456                                                                .
@echo . �˿ڣ�3306                                                              .
@echo .                                                                         .
@echo ...........................................................................


cd /d %~dp0
set startDir=%cd%
cd "%startDir%\mysql\bin"
call startup.bat
