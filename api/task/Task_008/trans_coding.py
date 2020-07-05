# author：wuziwei   
# @time:2020-07-05 18:02
# coding:-*- utf-8 -*-

def encoding(filename):
    with open('gbk编码.txt','r',encoding='gbk') as gbk_file,\
        open('utf8编码.txt','r',encoding='utf8') as utf8_file:
        gbk_file = gbk_file.read()
        utf8_file = utf8_file.read()
        merge = gbk_file + utf8_file

    with open(filename + '.txt','w',encoding='utf8') as new_file:
        new_file.write(merge)

if __name__ == '__main__':
    filename = input('请输入文件名称：')
    encoding(filename)