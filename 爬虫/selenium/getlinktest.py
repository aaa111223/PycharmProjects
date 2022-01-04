from selenium import webdriver
import time
from lxml import etree
import pymysql

driver = webdriver.Firefox()
driver.get('https://www.meijutt.tv/')
#最近更新
driver.get('https://www.meijutt.tv/new100.html')

#加载更多
# def load_mord(num):
#     #
#     for x in range(5):
#         js = "var q=document.documentElement.scrollTop=100000"
#         driver.execute_script(js)
#         time.sleep(2)
#     if num==0:
#         time.sleep(2)


#获取最近更新列表
def get_html():
    note_list=driver.find_element_by_class_name("top-list")
    html=note_list.get_attribute('innerHTML')
    return html

    print(html)
#点击第一个 <a href="/content/meiju25986.html" title="闪电侠第七季" target="_self" "="">闪电侠第七季</a>
driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/ul/li[1]/h5/a').click()
