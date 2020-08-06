# author：wuziwei   
# @time:2020-08-06 23:32
# coding:-*- utf-8 -*-

from app.Task.Task004.basePages import BasePage


class LoginPages(BasePage):
    def __init__(self):
        super(LoginPages, self).__init__()
        # 我的标签
        self.my_label = 'com.hpbr.bosszhipin:id/cl_tab_4'
        # 右上角设置图标
        self.right_set = 'com.hpbr.bosszhipin:id/iv_general_settings'
        # 账号与绑定选项
        self.user_bind = 'com.hpbr.bosszhipin:id/cl_item'
        # 修改密码
        self.change_password = "//*[@text='修改密码']"
        # 旧密码
        self.old_password = "//*[@text='输入旧密码']"
        # 新密码
        self.new_password = "//*[@text='请设置新密码（6-20位数字与字母组合）']"
        # 确认新密码
        self.verify_new_password = "//*[@text='再次输入新密码']"
        # 修改密码按钮
        self.change_password_botton = 'com.hpbr.bosszhipin:id/btn_save'
        # 校验密码修改成功元素
        self.success_assert = "//*[@text='手机号登录/注册']"
        # 账户密码登录
        self.chooser_user_login = "//*[@text='账户密码登录']"
        # 手机号输入框
        self.phone_input = 'com.hpbr.bosszhipin:id/et_phone'
        # 密码输入框
        self.password_input = 'com.hpbr.bosszhipin:id/et_password'
        # 登录按钮
        self.login_botton = 'com.hpbr.bosszhipin:id/btn_login'

    def my_label_ele(self):
        return self.driver.find_element_by_id(self.my_label)

    def right_set_ele(self):
        return self.driver.find_element_by_id(self.right_set)

    def user_bind_ele(self):
        return self.driver.find_element_by_id(self.user_bind)

    def change_password_ele(self):
        return self.driver.find_element_by_xpath(self.change_password)

    def old_password_ele(self):
        return self.driver.find_element_by_xpath(self.old_password)

    def new_password_ele(self):
        return self.driver.find_element_by_xpath(self.new_password)

    def verify_new_password_ele(self):
        return self.driver.find_element_by_xpath(self.verify_new_password)

    def change_password_botton_ele(self):
        return self.driver.find_element_by_id(self.change_password_botton)

    def success_assert_ele(self):
        return self.driver.find_element_by_xpath(self.success_assert)

    def chooser_user_login_ele(self):
        return self.driver.find_element_by_xpath(self.chooser_user_login)

    def phone_input_ele(self):
        return self.driver.find_element_by_id(self.phone_input)

    def password_input_ele(self):
        return self.driver.find_element_by_id(self.password_input)

    def login_botton_ele(self):
        return self.driver.find_element_by_id(self.login_botton)


LoginPages = LoginPages()
