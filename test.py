#coding=utf-8
#测试文件

import time
#from _typeshed import Self
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#通过js填写内容
def click_by_names(self, names, index=0):#通过js填写内容
        time.sleep(0.5)
        js = 'var q=document.getElementsByName("%s");q[%d].click()' % (names, index)
        self.driver.execute_script(js)
        
        

def main(self,object):
    print("hello world")
    driver = webdriver.Chrome()
    driver.get("url=http://www.baidu.com")
    time.sleep(1)
    #click_by_names("python公开课"，1)
 
        
        
        
    
        
        
        