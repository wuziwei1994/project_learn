# author：wuziwei   
# @time:2020-07-06 22:23
# coding:-*- utf-8 -*-

#调用cmd
import os
import subprocess

#返回值为0，运行cmd命令成功；返回值为1，运行cmd命令报错
# a = os.system('ipconfig')
#
# # print(a)
#
# #执行cmd命令，并将结果以字节字符串的方式返回，打印结果需要decode解码
# a1 = subprocess.check_output('ipconfig')
#
# # print(a1.decode('gbk'))

#非阻塞调用
a2 = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)
#修改为阻塞调用
a2.wait()
#接收cmd的输入出
output, err = a2.communicate()
print(output.decode('gbk'),err)
