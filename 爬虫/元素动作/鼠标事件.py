#coding=utf-8
from selenium import webdriver
# ���� ActionChains ��
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")

# ��λ��Ҫ��ͣ��Ԫ��
above = driver.find_element_by_link_text("����")
# �Զ�λ����Ԫ��ִ�������ͣ����
ActionChains(driver).move_to_element(above).perform()