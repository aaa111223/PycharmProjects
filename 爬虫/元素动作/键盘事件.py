#coding=utf-8
from selenium import webdriver
# ���� Keys ģ��
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# �������������
driver.find_element_by_id("kw").send_keys("seleniumm")

# ɾ���������һ��
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# ����ո��+���̡̳�
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("�̳�")

# ctrl+a ȫѡ���������
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x �������������
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ctrl+v ճ�����ݵ������
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# ͨ���س��������浥������
driver.find_element_by_id("su").send_keys(Keys.ENTER)
driver.quit()