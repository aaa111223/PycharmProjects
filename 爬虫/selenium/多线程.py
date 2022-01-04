#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.chrome.options import Options
import time,datetime
import platform

class LySpider():

    '''
    @:param date_str 查询日期
    @:param start_city 查询起始城市
    @:param arrive_city 查询抵达城市
    '''
    def __init__(self,date_str=None,start_city=None,arrive_city=None):
        self.date_str=date_str
        self.start_city=start_city
        self.arrive_city=arrive_city
        options = Options()
        #开启无头模式
        options.add_argument('--headless')
        #这个命令禁止沙箱模式，否则肯能会报错遇到chrome异常。
        options.add_argument('--no-sandbox')
        #建议加上user-agent，因为liunx下有时候会被当成手机版的，所以你会发现代码会报错
        num=str(float(random.randint(500,600)))
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/{}"
                 " (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/{}".format(num,num))
        options.add_argument('Origin=https://www.ly.com')
        sys_str = platform.system()
        if sys_str=="Linux":
            self.driver = webdriver.Chrome(executable_path='/home/chromedriver',
                                           chrome_options=options)
        else:
            self.driver = webdriver.Chrome()

#步骤3：已经初始化了相关信息以后，接下来就可以使用这个已经初始好的 driver 和查询参数进行模拟人工填充出发、抵达城市和日期，最后点击搜到按钮的过程。这里这里定义一个类方法，get_query_results()用于去模拟这个过程获取查询结果的html源码。示例代码如下：

 	'''
    通过selenium控制Chrome驱动，完成模拟人工输入查询地址和
    日期然后点击提交获取查询结果html的流程
    '''
    @property
    def get_query_results(self):

        '''
        隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        '''
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.ly.com/FlightQuery.aspx')
        locator = (By.ID, 'txtAirplaneCity1')
        try:
            # 显性等待
            WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located(locator))
            # 起始地城市input元素获取并清空值，然后填入城市名称,输入之后模拟按回车键
            txtAirplaneCity1 = self.driver.find_element_by_id("txtAirplaneCity1")
            # 通过js清空起始地城市值，并填充新的值
            js_clear_city1 = ''' document.getElementById('txtAirplaneCity1').value="" '''
            self.driver.execute_script(js_clear_city1)
            txtAirplaneCity1.send_keys(self.start_city)
            txtAirplaneCity1.send_keys(Keys.ENTER)

            # 抵达地城市input元素获取并清空值，然后填入城市名称，输入之后模拟按回车键
            txtAirplaneCity2 = self.driver.find_element_by_id("txtAirplaneCity2")
            txtAirplaneCity2.clear()
            # 通过js清空抵达地城市值，并填充新的值
            js_clear_city2 = ''' document.getElementById('txtAirplaneCity2').value="" '''
            self.driver.execute_script(js_clear_city2)
            txtAirplaneCity2.send_keys(self.arrive_city)
            txtAirplaneCity2.send_keys(Keys.ENTER)

            # 如果所查询的日期在当月范围内，则定位到日历插件中第1个div
            # 否则定位到第2个div，div1 表示当月，div2表示下一个月
            if is_same_month(self.date_str):
                # 定位到日历插件
                element_calendar = self.driver.find_elements_by_xpath(
                    "/html/body/div[17]/div/div[1]/div[1]/div/table/tbody/tr/td/span")
                for item in element_calendar:
                    if item.text == get_day(self.date_str):
                        item.click()
            else:
                element_calendar = self.driver.find_elements_by_xpath(
                    "/html/body/div[17]/div/div[1]/div[2]/div/table/tbody/tr/td/span")
                for item in element_calendar:
                    if item.text == get_day(self.date_str):
                        item.click()
            # 定位搜索按钮并模拟点击提交
            airplaneSubmit = self.driver.find_element_by_id("airplaneSubmit")
            airplaneSubmit.click()
            # 显性等待后，定位到机票查询结果div，然后获取div内的html
            locator_content = (By.ID, 'allFlightListDom_1')
            WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located(locator_content))
            flight_list_html=self.get_flight_list_dom()
            #返回结果
            data_list=[]
            '''
            此处判断返回的flight_list_html里面是否包含有机票信息，如果有
            直接返回此html代码，否则使用for循环从新尝试10次，每循环一次暂
            停一秒（这里为啥要这样写，因为实际情况中可能会存在网络延迟加载
            慢等原因导致获取不到内容）
            '''
            if flight_list_html:
                for item in flight_list_html:
                    data_list.append(item.get_attribute('innerHTML'))
            else:
                for x in range(10):
                    flight_list_html = self.get_flight_list_dom()
                    if flight_list_html:
                        for item in flight_list_html:
                            data_list.append(item.get_attribute('innerHTML'))
                        break
                    time.sleep(1)
            return data_list

        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()