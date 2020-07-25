# author：wuziwei   
# @time:2020-07-25 11:40
# coding:-*- utf-8 -*-

'''
解决拉钩或BOSS没有获取到公司名称的问题（已经获取到的同学忽略）
在上节课自动化BOSSAPP基础上完成以下操作
选择第一个搜索结果，点击进入详情，
获取职位名称下面的信息：地区、工作年限、学历
'''

from appium import webdriver

# 准备自动化配置信息
config = {
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号,写整数位即可
    'plathformVersion': '8',
    # 设备的名称--值可以随便写
    'deviceName': 'test0106',
    # 提供被测app的信息-包名，入口信息:
    # 1.打开被测app，2.命令行输入以下信息
    # adb shell dumpsys activity recents | findstr intent={
    'appPackage': 'com.hpbr.bosszhipin',
    'appActivity': '.module.launcher.WelcomeActivity',
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒，默认60s
    'newCommandTimeout': 6000,
    # 设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName': 'UiAutomator2',  # 或者UiAutomator1
    'skipServerInstallation': True  # 跳过UI2的安装，如果第一次运行程序，不要添加该配置
}

# 初始化driver对象-用于控制手机-启动被测应用
# IP-appium-server所在机器的网络ip，port-监听的端口号，path固定/wd/hub
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config)

driver.implicitly_wait(3)  # 稳定元素

# 点击放大镜
eles = driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')  # 先取所有符合条件的元素
# 找到第二个元素--放大镜
btn = eles[1]
btn.click()

# 搜索框输入职位信息
search_input = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')  # 输入参数

# 选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()

# 找到所有搜索结果，以列表存储
job_msg = driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')

# 选择第一个工作信息
first_job_msg = job_msg[0]
# 点击进入第一个工作信息
first_job_msg.click()

# 定位公司信息
job_msg_company_info = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_boss_title')
# 定位职位信息
job_name = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_job_name')
# 定位工作地元素
job_msg_address = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_location')
# 定位工作年限
job_msg_years = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_work_exp')
# 定位学历要求
job_msg_education = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_degree')
# 定位薪资信息
job_salary = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_job_salary')
# 定位返回按钮
back_botton = driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_back')

print(
    f'第一个搜索职位：{job_msg_company_info.text}|{job_name.text}|{job_msg_address.text}|{job_msg_years.text}|{job_msg_education.text}|{job_salary.text}')
driver.quit()
