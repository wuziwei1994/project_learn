# author：wuziwei   
# @time:2020-07-08 20:57
# coding:-*- utf-

from selenium import webdriver

# 创建浏览器对象
driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')
# 访问网址
driver.get('http://b.local.weicantimes.com')
num = '539848'
account = 'wct'
password = '123456'

def login_():
    # driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[1]/div/input').send_keys(num)
     driver.find_element_by_xpath('document.querySelector("#app > div.container-login > div.container-login-main > div.login-main > form > div:nth-child(2) > div > input")').send_keys(account)
    # driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[3]/div/input').send_keys(password)

login_()
