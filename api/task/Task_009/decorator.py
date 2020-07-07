import random
import string

user_dict = {'user1': '123', 'user2': '123'}
#封装一个登陆验证并返回token

def get_login1(user,password)
    def get_login(f):
        user = input('输入账号')
        password = input('输入密码')
        @get_login
        def get_token(user,password):
            token = ''.join(random.sample(string.ascii_letters + string.digits, 32)).lower()
            if user in user_dict and password == user_dict[user]:
                return token
            else:
                return '账号或密码错误'

print(get_login())

# def my_log():
#     print('this is my_log')
#
# def my_name(name):
#     print('欢迎登陆',name)
#
# def my_shopping_mall():
#     print('商城购物')
#
# while True:
#     choose_num = input('\n\n1、查看日志\n2、我的信息\n3、我的商城\n请输入操作选项(输入q退出)>>>')
#     if choose_num == 'q' or choose_num == 'Q':
#         break
#     elif choose_num == '1':
#         my_log()
#     elif choose_num == '2':
#         my_name('张三')
#     elif choose_num == '3':
#         my_shopping_mall()
#     else:
#         print('输入不合法')