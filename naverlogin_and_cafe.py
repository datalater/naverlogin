# 네이버 로그인 url = 'https://nid.naver.com/nidlogin.login'
# 네이버 카페 자기소개서 url = 'http://cafe.naver.com/hrbrown/ArticleList.nhn?search.clubid=24169464&search.menuid=18&search.boardtype=L'

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import re

url = 'https://nid.naver.com/nidlogin.login'
cafe_url = 'http://cafe.naver.com/hrbrown.cafe?iframe_url=/hrbrown/ArticleList.nhn%3Fsearch.clubid=24169464%26search.menuid=18%26search.boardtype=L'
user_id = 'winner1231'
user_pwd = 'qwer1234'

#----------------네이버로그인----------------#

driver = webdriver.Chrome('C:/Users/hufs/Downloads/download/lawjmc/chromedriver')  # Optional argument, if not specified will search path.
driver.get(url)
driver.find_element_by_id('id').send_keys(user_id)
driver.find_element_by_id('pw').send_keys(user_pwd)

btn = driver.find_element_by_class_name('btn_global')
btn.click()

#----------------네이버카페파싱----------------#

driver.get(cafe_url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


#driver.close()
