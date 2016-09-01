from bs4 import BeautifulSoup
import re

base_url = 'http://cafe.naver.com/hrbrown'

file_path1 = 'C:/Users/hufs/Downloads/download/lawjmc/naverlogin/navercafe.html'
soup = BeautifulSoup(open(file_path1),"html.parser")

table = soup.find("form", {"name":"ArticleList"})

for a_tag in table.find_all(href=re.compile('ArticleRead')): # 자기소개서 a태그 추출
    for title in a_tag(string=re.compile('자기소개서')): # 자기소개서 제목 추출
        print(title)
        href_url= base_url+a_tag['href']
        print(href_url)

        print("#-----------자기소개서 태그와 제목 추출-----------#")

        #----------href이동----------#
        
file_path2 = 'C:/Users/hufs/Downloads/download/lawjmc/naverlogin/navercafe_article.html'
soup = BeautifulSoup(open(file_path2),"html.parser")

file_extension = '.html'

new_file = open('C:/Users/hufs/Downloads/download/lawjmc/naverlogin/'+title+file_extension, 'w', encoding='UTF-8')
new_file.write(str(soup))
new_file.close()
        
     
    

# 자기소개서 게시판 페이지 이동 url
# /ArticleList.nhn?search.boardtype=L&search.menuid=18&search.questionTab=A&search.clubid=24169464&search.totalCount=151&search.page=2
