#�ȸ�����ʾ����

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
#ʹ�ùȸ�����
driver = webdriver.Chrome(chrome_options=chrome_options)
#��url
driver.get("https://www.baidu.com/")

#�������ʾ����

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument('--headless')
#ʹ�û������
driver = webdriver.Firefox(firefox_options=firefox_options)
#��url
driver.get("https://www.baidu.com/")