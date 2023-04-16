# encoding=utf-8
# import necessary libraries
from ssl import SSLError

import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import time
import urllib.parse
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# from selenium import webdriver


def scrape_baidu(query):
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(2)
    # 最大化浏览器并输出浏览器的大小和位置坐标
    driver.maximize_window()
    time.sleep(2)
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "wd")))
    #encoded_query = urllib.parse.quote(query)

    #name = query.encode(encoding='utf-8')
    search_box.send_keys(query)
    search_box.submit()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = []
    for result in soup.select('div.result'):
        try:
            link = result.select_one('h3 a')
            title = link.get_text()
            url = link['href']
            results.append({'title': title, 'url': url})
            #print(results)
        except:
            pass
    driver.quit()
    return results


# define function to save search results to MySQL database
def save_to_database(query: str, results: List[Dict[str, str]]):
    # establish connection to MySQL database
    cnx = mysql.connector.connect(user='root', password='1qazxsw2',
                                  host='localhost', database='xs_db')
    # create cursor object
    cursor = cnx.cursor()
    # define query to insert search results into database
    add_results = "INSERT INTO search_results(query, title, url, date) VALUES (%s, %s, %s, %s)"
    # get today's date
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # execute query to insert search results into database
    for result in results:
        cursor.execute(add_results, (query, result['title'], result['url'], now))
    # commit changes to database
    cnx.commit()
    # close cursor and connection
    cursor.close()
    cnx.close()

# example usage
query = input("输入查询内容: ")
encoded_query = urllib.parse.quote(query)
results = scrape_baidu(encoded_query)
print(f"包括 {len(results)} 结果，查询: {query}")
save_to_database(query, results)

