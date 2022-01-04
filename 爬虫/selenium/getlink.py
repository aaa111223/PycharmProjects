from selenium import webdriver
import time
from lxml import etree
import pymysql

driver = webdriver.Firefox()
#天天看美剧网
#driver.get('https://www.ttkmj.org/')
#最近更新
driver.get('https://www.meijutt.tv/new100.html')

#加载更多
def load_mord(num):
    #
    for x in range(5):
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        time.sleep(2)
    if num==0:
        time.sleep(2)

#获取最近更新列表
def get_html():
    note_list=driver.find_element_by_class_name("top-list")
    html=note_list.get_attribute('innerHTML')
    return html

#传入内容网页源码，使用xpath提取信息标题、简介、发布昵称  /html/body/div[3]/div[4]/div[1]/ul/li[1]/h5/a
def extract_data(content_html):
    html = etree.HTML(content_html)
    title_list =html.xpath('//li//a[@class="title"]/text()')
    abstract_list=html.xpath('//li//p[@class="abstract"]/text()')
    nickname_list=html.xpath('//li//a[@class="nickname"]/text()')
    data_list=[]
    for index,x in enumerate(title_list):
        item={}
        item["title"]=title_list[index]
        item["abstract"] = abstract_list[index]
        item["nickname"] = nickname_list[index]
        data_list.append(item)
    return data_list

#保存到mysql数据库
def insert_data(sql):
    db = pymysql.connect(host="127.0.0.1", user="root", password="1qazxsw2", database="xs_db", port=3306,charset="utf8")
    try:
        cursor = db.cursor()
        return cursor.execute(sql)
    except Exception as ex:
        print(ex)
    finally:
        db.commit()
        db.close()

#模拟点击10次阅读更多按钮
for x in range(2):
    print("模拟点击加载更多第 {} 次".format(str(x)))
    load_mord(x)
    time.sleep(1)

results=extract_data(get_html())
for item in results:
        sql="insert into tb_test(title,abstract,nickname) values('%s','%s','%s')" \
        ""%(item["title"],item["abstract"],item["nickname"])
        print(item)
        insert_data(sql)