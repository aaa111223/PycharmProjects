#coding=utf-8
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# ��������Ϊ���ص�
print("�����������480����800��ʾ")
browser.set_window_size(480, 800)
browser.quit()