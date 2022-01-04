#谷歌驱动示例：

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
#使用谷歌驱动
driver = webdriver.Chrome(chrome_options=chrome_options)
#打开url
driver.get("https://www.baidu.com/")

#火狐驱动示例：

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument('--headless')
#使用火狐驱动
driver = webdriver.Firefox(firefox_options=firefox_options)
#打开url
driver.get("https://www.baidu.com/")