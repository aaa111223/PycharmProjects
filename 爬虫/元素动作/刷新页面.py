from selenium import webdriver

browser = webdriver.Chrome()

#���ʰٶ���ҳ
url= 'http://www.baidu.com'
browser.get(url)
#ˢ�µ�ǰҳ��
browser.refresh()