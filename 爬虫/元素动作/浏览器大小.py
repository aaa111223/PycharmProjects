#coding=utf-8
# 增加修饰
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

sleep(2)
# 将窗口大小实例化
size_Dict = driver.get_window_size()
# 打印浏览器的宽和高
print("当前浏览器的宽：", size_Dict['width'])
print("当前浏览器的高：", size_Dict['height'])
# 设置浏览器的大小
driver.set_window_size(width=500, height=500, windowHandle="current")
# windowHandle = "current" 控制当前窗口的意思

sleep(2)
# 将窗口位置实例化
position = driver.get_window_position()
# 打印窗口坐标
print(position)
print("浏览器所在位置的横坐标：", position["x"])
print("浏览器所在位置的纵坐标：", position["y"])
# 设置窗口位置并打印位置坐标
driver.set_window_position(x=100, y=200)
print(driver.get_window_position())


sleep(2)
# 最大化浏览器并输出浏览器的大小和位置坐标
driver.maximize_window()
print(driver.get_window_size())
print(driver.get_window_position())


sleep(2)
driver.quit()