# author：wuziwei   
# @time:2020-08-06 23:35
# coding:-*- utf-8 -*-

'''
Appium 作业 4
在上节课(day3)代码基础上完成新密码的验证工作
1.使用新密码登录
2.要求密码不要写在代码里面
'''

from app.Task.Task004.loginPages import LoginPages
from app.Task.Task004.config import old_password, new_password, user_name
import time


class TestVerifyPassword:

    def test_verify_password_test(self):
        '''1.进入我的标签'''
        LoginPages.my_label_ele().click()
        '''2.点击右上角设置图标'''
        LoginPages.right_set_ele().click()
        '''3.进入账号与绑定'''
        LoginPages.user_bind_ele().click()
        '''4.进入设置密码'''
        LoginPages.change_password_ele().click()
        '''5.完成密码设置'''
        # 输入旧密码
        LoginPages.old_password_ele().send_keys(f'{old_password}')
        # 输入新密码
        LoginPages.new_password_ele().send_keys(f'{new_password}')
        # 确认新密码
        LoginPages.verify_new_password_ele().send_keys(f'{new_password}')
        # 点击修改密码
        LoginPages.change_password_botton_ele().click()
        time.sleep(1)
        assert '手机号登录' in LoginPages.success_assert_ele().text
        print(f'密码修改成功,新密码是：{new_password}')

    def test_new_password_login(self):
        if '手机号登录' in LoginPages.success_assert_ele().text:
            LoginPages.chooser_user_login_ele().click()
            if '133' in LoginPages.phone_input_ele().text:
                LoginPages.password_input_ele().send_keys(new_password)
                LoginPages.login_botton_ele().click()
            else:
                LoginPages.phone_input_ele().send_keys(user_name)
                LoginPages.new_password_ele().send_keys(new_password)
                LoginPages.login_botton_ele().click()
            assert LoginPages.my_label_ele()
            print('登录成功')
