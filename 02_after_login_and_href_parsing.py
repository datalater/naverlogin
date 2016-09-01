from bs4 import BeautifulSoup
import re

base_url = 'http://cafe.naver.com/hrbrown'

file_path = 'C:/Users/hufs/Downloads/download/lawjmc/naverlogin/navercafe.html'
soup = BeautifulSoup(open(file_path),"html.parser")

table = soup.find("form", {"name":"ArticleList"})

for a_tag in table.find_all(href=re.compile('ArticleRead')): # 자기소개서 a태그 추출
    for title in a_tag(string=re.compile('자기소개서')): # 자기소개서 제목 추출
        print(title)
        href_url= base_url+a_tag['href']
        print(href_url)

        #----------href이동----------#
        #driver.get(href_url)
        
     
    

# 자기소개서 게시판 페이지 이동 url
# /ArticleList.nhn?search.boardtype=L&search.menuid=18&search.questionTab=A&search.clubid=24169464&search.totalCount=151&search.page=2
