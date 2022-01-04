from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()
driver.quit()