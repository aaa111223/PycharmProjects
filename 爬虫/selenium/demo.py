from selenium import webdriver
import time
from lxml import etree
import pymysql

driver = webdriver.Chrome()
# 天天看美剧网
# driver.get('https://www.ttkmj.org/')
# 最近更新
#driver.get('https://www.meijutt.tv/new100.html')
driver.get('https://www.baidu.com')

time.sleep(2)
# 最大化浏览器并输出浏览器的大小和位置坐标
driver.maximize_window()
print(driver.get_window_size())
print(driver.get_window_position())

# 加载更多
def load_mord(num):
    #
    for x in range(5):
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        time.sleep(2)
        driver.refresh()
        print("refresh")
    if num == 0:
        time.sleep(2)


# 获取最近更新列表
def get_html():
    # note_list = driver.find_element_by_class_name("warp") /html/body/div[2]/div[3]
    note_list = driver.find_element("class name","wrapper_new")
    print("=========  ", note_list)

    html = note_list.get_attribute('innerHTML')
    print("html:",html)
    html1 = etree.HTML(html)
# /html/body/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/a
    list = html1.xpath('/html/body/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[3]/div/a')
    print("list:",list)

    # print(note_list)
    return html


# 传入内容网页源码，使用xpath提取信息标题、简介、发布昵称  /html/body/div[3]/div[4]/div[1]/ul/li[1]/h5/a
def extract_data(content_html):
    html = etree.HTML(content_html)
    print("aaaaaaaa",html)
    # title_list =html.xpath('//li//a[@class="title"]/text()')
    title_list = html.xpath('//html/body/div[2]/div[4]/div[1]/ul/li[1]/h5/a')
    print("********* ", title_list)
    abstract_list = html.xpath('//li//p[@class="abstract"]/text()')
    nickname_list = html.xpath('//li//a[@class="nickname"]/text()')
    data_list = []
    for index, x in enumerate(title_list):
        item = {}
        item["title"] = title_list[index]
        item["abstract"] = abstract_list[index]
        item["nickname"] = nickname_list[index]
        data_list.append(item)
    return data_list


# 模拟点击10次阅读更多按钮
# for x in range(2):
#     print("模拟点击加载更多第 {} 次".format(str(x)))
#     load_mord(x)
#     time.sleep(1)

results = extract_data(get_html())
print("results:", results)

for item in results:
    localtime = time.asctime(time.localtime(time.time()))
    sql = "insert into tb_test(title,abstract,nickname) values('%s','%s','%s','%s')" \
          "" % (item["title"], item["abstract"], item["nickname"], localtime)
    insert_data(sql)
