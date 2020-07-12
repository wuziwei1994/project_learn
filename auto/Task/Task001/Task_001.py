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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')

url = driver.get('https://m.weibo.cn/')

time.sleep(1.5)
ele = driver.find_element_by_css_selector(
    '#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > i').click()

time.sleep(1.5)
ele1 = driver.find_element_by_css_selector(
    '#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4').click()

ele3 = WebDriverWait(driver, 3, 0.5).until(
    expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, 'card-title')
    )
)
ele4 = driver.find_element_by_css_selector(
    '#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div')

ele5 = ele4.find_elements_by_class_name('card4')

for one in ele5:

    icon = one.find_elements_by_class_name('m-link-icon')

    if icon:
        img = icon[-1].find_element_by_tag_name('img')
        src = img.get_attribute('src')
        if 'hot' in src:
            hotType = '热'
            # 获取热搜文本
            hotText = one.find_element_by_class_name("m-text-cut").text
            print('{}: {}'.format(hotType, hotText))

        elif 'new' in src:
            hotType = '新'
            # 获取热搜文本
            hotText = one.find_element_by_class_name("m-text-cut").text
            print('{}: {}'.format(hotType, hotText))

        elif 'plus' in src:
            hotType = 'plus'
            # 获取热搜文本
            hotText = one.find_element_by_class_name("m-text-cut").text
            print('{}: {}'.format(hotType, hotText))

        elif 'fei' in src:
            hotType = '沸'
            # 获取热搜文本
            hotText = one.find_element_by_class_name("m-text-cut").text
            print('{}: {}'.format(hotType, hotText))

driver.quit()
