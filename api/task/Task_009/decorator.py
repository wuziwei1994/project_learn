# author：wuziwei   
# @time:2020-07-07 23:08
# coding:-*- utf-8 -*-
import random,string

user_dict = {'user1':'123','user2':'123'}
token = ''

def auth(func):
    def inner(*args):
        global token
        if token:
            func(args)
        else:
            user = input('请输入账户')
            password = input('请输入密码')
            if user in user_dict and user_dict[user] == password:
                func(args)
                token = ''.join(random.sample(string.ascii_letters + string.digits,32)).lower()
    return inner()

@auth
def my_log():
    print('this is my_log')
@auth
def my_name(name):
    print('欢迎登陆',name)
@auth
def my_shopping_mall():
    print('商城购物')

while True:
    choose_num = input('\n\n1、查看日志\n2、我的信息\n3、我的商城\n请输入操作选项（输入q退出）>>>')
    if choose_num == 'q' or choose_num == 'Q':
        break
    elif choose_num == '1':
        my_log()
    elif choose_num == '2':
        my_name('张三')
    elif choose_num == '3':
        my_shopping_mall()
    else:
        print('输入不合法')


