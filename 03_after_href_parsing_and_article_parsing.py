from bs4 import BeautifulSoup
import re

base_url = 'http://cafe.naver.com/hrbrown'

file_path2 = 'C:/Users/hufs/Downloads/download/lawjmc/naverlogin/navercafe_article.html'
soup = BeautifulSoup(open(file_path2),"html.parser")

title = 'temporary'
file_extension = '.html'

new_file = open('C:/Users/hufs/Downloads/download/lawjmc/naverlogin/'+title+file_extension, 'w', encoding='UTF-8')
new_file.write(str(soup))
new_file.close()


        
     
    

# 자기소개서 게시판 페이지 이동 url
# /ArticleList.nhn?search.boardtype=L&search.menuid=18&search.questionTab=A&search.clubid=24169464&search.totalCount=151&search.page=2
