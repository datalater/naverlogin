# 네이버 로그인 url = 'https://nid.naver.com/nidlogin.login'
# 네이버 카페 자기소개서 url = 'http://cafe.naver.com/hrbrown/ArticleList.nhn?search.clubid=24169464&search.menuid=18&search.boardtype=L'
# @gram
# driver = webdriver.Chrome('C:\Python34\jmcproject/chromedriver.exe')
# @law
# driver = webdriver.Chrome('C:/Users/hufs/Downloads/download/lawjmc/chromedriver')

import time
import requests

from bs4 import BeautifulSoup
import re

head={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

login_url = 'https://nid.naver.com/nidlogin.login'
test_page = 'http://cafe.naver.com/sam2016group11/17'

base_url = 'http://cafe.naver.com/sam2016group11'
cafe_url = 'http://cafe.naver.com/sam2016grou11/ArticleRead.nhn?clubid=28360999&page=1&menuid=3&boardtype=L&articleid=6&referrerAllArticles=false'

user_id = 'the7mincheol'
user_pwd = '(j2131231)'

'''
base_url = 'http://cafe.naver.com/hrbrown'
cafe_url = 'http://cafe.naver.com/hrbrown//ArticleList.nhn?search.boardtype=L&search.menuid=18&search.questionTab=A&search.clubid=24169464&search.totalCount=151&search.page=1&search.clubid=24169464'

user_id = 'winner1231'
user_pwd = 'qwer1234'
'''

current_session = requests.session()

params = {
    'id':user_id,
    'pw':user_pwd,
    'enctp': '1',
    #'encpw':'',
    #'encnm':'',
    'svctype': '0',
    'viewtype': '0',
    'locae': 'ko_KR',
    'smart_LEVEL': '1',
    'url': 'http://www.naver.com'
    }

current_session.post(login_url, data=params, headers=head)
current_session.get(test_page,headers=head)

page = current_session.get(test_page,headers=head)

html = BeautifulSoup(page.text, "html.parser")

print(html)
