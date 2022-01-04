#config = utf-8
from selenium import webdriver
import time

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("http://www.126.com")


#driver.switch_to.frame('x-URS-iframe')
#//*[@id="x-URS-iframe1612020927529.8464"]

driver.find_element_by_xpath("//*[@id=\"x-URS-iframe*\"]")


# print("企业邮箱")
# driver.find_element_by_xpath("/html/body/div[1]/div[2]/a[1]").click()
# time.sleep(3)
# driver.find_element_by_tag_name("_blank")
# driver.find_element_by_class_name("btn-login").click()
# #driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/a[2]").click()
# #//*[@id="switchNormalCtrl"]
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id=\"switchNormalCtrl\"]").click
# # 输入用户
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id=\"accname\"]").clear()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id=\"accname\"]").send_keys("lyl_sc")



driver.find_element_by_name("email").click()
print("输入email")
driver.find_element_by_name("email").send_keys("lyl_sc")
print("清空passwd")
driver.find_element_by_name("password").clear()
print("输入passwd")
driver.find_element_by_name("password").send_keys("123456")
print("点击登录")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

driver.quit()