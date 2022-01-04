# coding=utf-8
# 模拟登陆CSDN博客
import time
from selenium import webdriver

#使用谷歌驱动
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
#打开登录页面
driver.get("https://passport.csdn.net/account/login")
#由于有可能存在网络加载慢等原因，所以这里先加载时暂停10秒（这个暂停时间具体根据实际情况	设置）之后再去获取表单元素
time.sleep(10)
#由于CSDN登录页面默认是扫码登录，所有我们打开登录页面之后需要模拟先切换到账号密码登录，	然后再使用selenium自动填充账号密码登录
# driver.find_element_by_class_name("text-tab border-right").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a").click()
#先暂停3秒，以防止页面为加载完成导致获取不到用户名密码元素
time.sleep(3)
driver.find_element_by_id("tabTwo").click()
time.sleep(3)
#-----自动填充用户密码-----
#通过id获取username元素，并向其中填入用户名
login_username = driver.find_element_by_id('phone')
time.sleep(1)
login_username.send_keys('15210987982')
time.sleep(1)
#通过id获取password元素，并向其中填入密码
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[5]/div/div[4]/div/button").click()
time.sleep(15)
# login_passwd=driver.find_element_by_id('password-number')
# login_passwd.send_keys('1428936720lyl')
#获取登录按钮，模拟点击提交
driver.find_element_by_class_name("btn btn-primary").click()

#使用Selenium模拟百度搜索
# import time
# from selenium import webdriver
#
# #使用谷歌驱动
# driver = webdriver.Firefox()
# #打开登录页面
# driver.get("selenium")
# #由于有可能存在网络加载慢等原因，所以这里先加载时暂停2秒（这个暂停时间具体根据实际情况	设置）之后再去获取表单元素
# time.sleep(2)
# #定位到搜索框
# kw=driver.find_element_by_id("kw")
# #向定位到的input填入值
# kw.send_keys("Python")
# #定位su提交按钮
# su=driver.find_element_by_id("su")
# #模拟点击提交
# su.click()