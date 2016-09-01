# 네이버 로그인 url = 'https://nid.naver.com/nidlogin.login'
# 네이버 카페 자기소개서 url = 'http://cafe.naver.com/hrbrown/ArticleList.nhn?search.clubid=24169464&search.menuid=18&search.boardtype=L'
# @gram
# driver = webdriver.Chrome('C:\Python34\jmcproject/chromedriver.exe')
# @law
# driver = webdriver.Chrome('C:/Users/hufs/Downloads/download/lawjmc/chromedriver')

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import re

login_url = 'https://nid.naver.com/nidlogin.login'
base_url = 'http://cafe.naver.com/hrbrown'
cafe_url = 'http://cafe.naver.com/hrbrown//ArticleList.nhn?search.boardtype=L&search.menuid=18&search.questionTab=A&search.clubid=24169464&search.totalCount=151&search.page=1&search.clubid=24169464'

user_id = 'winner1231'
user_pwd = 'qwer1234'

#----------------네이버로그인----------------#

driver = webdriver.Chrome('C:\Python34\jmcproject/chromedriver.exe')
driver.get(login_url)
driver.find_element_by_id('id').send_keys(user_id)
driver.find_element_by_id('pw').send_keys(user_pwd)

btn = driver.find_element_by_class_name('btn_global')
btn.click()

#----------------네이버카페.제목_href파싱----------------#

driver.get(cafe_url)

ActionChains(driver).key_down(Keys.F12).key_up(Keys.F12).perform()

#element = driver.find_element_by_xpath("//div[@id='main-area']")
#ActionChains(driver).context_click(element).perform()

'''

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

table = soup.find("form", {"name":"ArticleList"})

for a_tag in table.find_all(href=re.compile('ArticleRead')): # 자기소개서 a태그 추출
    for title in a_tag(string=re.compile('자기소개서')): # 자기소개서 제목 추출
        print(title)
        href_url= base_url+a_tag['href']
        print(href_url)

        print("#-----------자기소개서 태그와 제목 추출-----------#")

#----------------네이버카페.내용파싱및파일생성----------------#

        driver.get(href_url)

        html = driver.page_source
        soup = BeautifulSoup(html,"html.parser")

        file_extension = '.html'

        new_file = open('C:/Users/hufs/Downloads/download/lawjmc/naverlogin/'+title+file_extension, 'w', encoding='UTF-8')
        new_file.write(str(soup))
        new_file.close()
    
driver.get(href_url)
#driver.close()

'''
