# author：wuziwei   
# @time:2020-07-25 15:24
# coding:-*- utf-8 -*-

from appium import webdriver

config = {
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号,写整数位即可
    'plathformVersion': '9',
    # 设备的名称--值可以随便写
    'deviceName': 'test0106',
    # 提供被测app的信息-包名，入口信息:
    # 1.打开被测app，2.命令行输入以下信息
    # adb shell dumpsys activity recents | findstr intent={
    'appPackage': 'com.weicantimes.weican.intl',
    'appActivity': 'com.weicantimes.module.login.mvp.ui.activity.WelcomeActivity',
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

ele = driver.find_element_by_id('com.weicantimes.weican.intl:id/acn')
ele.click()
user = driver.find_elements_by_id('com.weicantimes.weican.intl:id/aem')
button = user[1]
button.click()
password = driver.find_element_by_id('com.weicantimes.weican.intl:id/a01')
password.click()
password.click()
password.click()
password.click()
password.click()
password.click()

