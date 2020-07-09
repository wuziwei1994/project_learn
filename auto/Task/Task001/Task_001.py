# author：wuziwei   
# @time:2020-07-09 22:34
# coding:-*- utf-8 -*-

'''
访问：https://m.weibo.cn/
点击：大家都在搜

找到：微博热搜榜

点击：微博热搜榜

找到：实时热点，每分钟更新一次
将其中带有 热、沸、新字样的热搜信息获取到，并注明属于三种当中的哪一种

'''

from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')

url = driver.get('https://m.weibo.cn/')
lens = [0,1,2]
click_search = driver.find_element_by_class_name('m-search').click()
time.sleep(1)
click_hot_search = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div/div[8]/div/div/h4').click()
time.sleep(1)
find_hot = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/h2').text
time.sleep(1)
find_all_hot_list = driver.find_element_by_class_name('card-list')
time.sleep(1)
find_all_hot_card4 = find_all_hot_list.find_element_by_class_name('card4')
time.sleep(1)
for one in find_all_hot_card4:
    icon = driver.find_element_by_link_text('m-link-icon')
    if icon:
        img = icon[0].f