# author：wuziwei   
# @time:2020-08-03 23:22
# coding:-*- utf-8 -*-

boss = {
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

old_password = 'Ceshi123'
new_password = 'Ceshi1234'
