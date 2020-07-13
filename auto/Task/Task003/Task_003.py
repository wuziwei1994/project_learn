# author：wuziwei   
# @time:2020-07-12 21:03
# coding:-*- utf-8 -*-
'''
http://vip.ytesting.com/q.do?a&id=ff8080817238543f01723b6246cc011e

登录 http://www.51job.com
    点击高级搜索
    输入搜索关键词 python
    地区选择 杭州
    职能类别 选 计算机软件 -> 高级软件工程师
    公司性质选 外资 欧美
    工作年限选 1-3 年

搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息

    Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
    Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
    on开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27

'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'D:\project_learn\chromedriver.exe')

url = driver.get('http://www.51job.com')
driver.maximize_window()

driver.implicitly_wait(3)

# 点击高级搜索
more_search = driver.find_element_by_css_selector('.more').click()

# 点击选择地区
driver.find_element_by_css_selector('.el.on >p.addbut > input').click()
# 取消当前定位
driver.find_element_by_id('work_position_click_ip_location_000000_030800').click()

# 选择 杭州
time.sleep(2)
city_id = driver.find_elements_by_css_selector('.sbar >li')
for id in city_id:
    if 'H' not in id.text:
        continue
    id.click()

city_choose = driver.find_element_by_id(
    'work_position_click_center_right_list_category_220200_080200').click()

subimt = driver.find_element_by_css_selector('#work_position_click_bottom >#work_position_click_bottom_save').click()

# 职能类别 选 计算机软件 -> 高级软件工程师
driver.find_element_by_css_selector('#funtype_div >span').click()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()

time.sleep(3)
driver.find_element_by_id('indtype_click').click()
driver.find_element_by_id('indtype_click_center_right_list_category_01_01').click()
driver.find_element_by_id('indtype_click_bottom_save').click()

# 公司性质选 外资 欧美
time.sleep(1)
driver.find_element_by_id('cottype_list').click()
list = driver.find_elements_by_css_selector('#cottype_list >.ul span ')
for one in list:
    if '外资（欧美）' in one.text:
        one.click()
        break

# 工作年限选 1-3 年
time.sleep(1)
driver.find_element_by_id('workyear_list').click()
years_list = driver.find_elements_by_css_selector('#workyear_list >.ul span')
for one in years_list:
    if '1-3年' in one.text:
        one.click()
        break

# 输入搜索关键词 python
time.sleep(1)
input_python = driver.find_element_by_css_selector('.el.on >p.ipt >input').send_keys('python')

# 点击搜索
driver.find_element_by_css_selector('.btnbox.p_sou >span').click()

# 点击外层搜索
time.sleep(2)
driver.find_element_by_css_selector('.dw_search_in >.p_but').click()

# 点击按时间排序
time.sleep(2)
driver.find_element_by_css_selector('.rt.order_time >a').click()

# 获取表格表头
find_job_list_title = driver.find_elements_by_css_selector('.dw_table >.el.title>span')
job_list_title = [title.text for title in find_job_list_title]
print('|'.join(job_list_title))

# 获取工作信息
job_list = driver.find_elements_by_css_selector('#resultList >.el')
for job in job_list:
    if 'title' in job.get_attribute("class"):
        continue
    job_info = job.find_elements_by_css_selector('span')
    job_info_list = [info.text for info in job_info]
    print('|'.join(job_info_list))

time.sleep(5)
driver.quit()
