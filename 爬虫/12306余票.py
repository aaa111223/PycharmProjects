from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开12306网站
driver.get("https://www.12306.cn/index/")

# 等待页面加载完成
time.sleep(5)
driver.maximize_window()
time.sleep(2)
# 点击登录按钮
login_button = driver.find_element_by_xpath("//a[@id='login_user']")
login_button.click()

# 等待登录框出现
time.sleep(5)

# 输入用户名和密码
username_input = driver.find_element_by_xpath("//input[@id='username']")
username_input.send_keys("xxxxx")
password_input = driver.find_element_by_xpath("//input[@id='password']")
password_input.send_keys("xxxxx")

# 点击登录按钮
login_button = driver.find_element_by_xpath("//a[@id='loginSub']")
login_button.click()

# 等待登录完成
time.sleep(10)

# 打开车票查询页面
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")

# 输入出发地、目的地和日期
from_input = driver.find_element_by_xpath("//input[@id='fromStationText']")
from_input.clear()
from_input.send_keys("北京")
from_input.send_keys(Keys.RETURN)

to_input = driver.find_element_by_xpath("//input[@id='toStationText']")
to_input.clear()
to_input.send_keys("长春")
to_input.send_keys(Keys.RETURN)

date_input = driver.find_element_by_xpath("//input[@id='train_date']")
date_input.clear()
date_input.send_keys("2022-01-01")
date_input.send_keys(Keys.RETURN)

# 等待查询结果出现
time.sleep(5)

# 获取车票余量信息
ticket_info = driver.find_element_by_xpath("//tbody[@id='queryLeftTable']/tr[1]/td[12]")
print(ticket_info.text)

# 关闭浏览器
driver.quit()
