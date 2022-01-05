#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# ��������ĳߴ�
size = driver.find_element_by_id('kw').size
print(size)
# ���ذٶ�ҳ��ײ�������Ϣ
text = driver.find_element_by_id("cp").text
print(text)
# ����Ԫ�ص�����ֵ�� ������ id��name��type ��������������
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)
# ����Ԫ�صĽ���Ƿ�ɼ��� ���ؽ��Ϊ True �� False
result = driver.find_element_by_id("kw").is_displayed()
print(result)
driver.quit()