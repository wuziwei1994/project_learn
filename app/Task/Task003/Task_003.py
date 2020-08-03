# author：wuziwei   
# @time:2020-08-03 22:42
# coding:-*- utf-8 -*-

'''
Appium 作业 3
自动化BOSS
尝试自动化方式完成以下操作
1.进入我的标签
2.点击右上角设置图标
3.进入账号与绑定
4.进入设置密码
5.完成密码设置
#利用该方法获取页面的XML信息，自行进行元素定位
driver.page_source
'''

from appium import webdriver
from app.Task.Task003.config import boss, old_password, new_password
import time

# 初始化driver对象-用于控制手机-启动被测应用
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', boss)

driver.implicitly_wait(3)  # 稳定元素

'''1.进入我的标签'''
driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()
'''2.点击右上角设置图标'''
driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()
'''3.进入账号与绑定'''
driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()
'''4.进入设置密码'''
driver.find_element_by_xpath("//*[@text='修改密码']").click()
'''5.完成密码设置'''
# 输入旧密码
driver.find_element_by_xpath("//*[@text='输入旧密码']").send_keys(f'{old_password}')
# 输入新密码
driver.find_element_by_xpath("//*[@text='请设置新密码（6-20位数字与字母组合）']").send_keys(f'{new_password}')
# 确认新密码
driver.find_element_by_xpath("//*[@text='再次输入新密码']").send_keys(f'{new_password}')
# 点击修改密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()
time.sleep(3)

'''校验是否修改成功'''
ele = driver.find_element_by_xpath("//*[@text='手机号登录/注册']")
assert ele

print(f'密码修改成功，新密码是：{new_password}')

driver.quit()
