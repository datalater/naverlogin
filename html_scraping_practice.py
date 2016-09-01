from bs4 import BeautifulSoup
import re

base_url = 

file_path = 'C:/Users/hufs/Downloads/download/lawjmc/naverlogin/navercafe.html'
soup = BeautifulSoup(open(file_path),"html.parser")

table = soup.find("form", {"name":"ArticleList"})

for a_tag in table.find_all(href=re.compile('ArticleRead')): # 자기소개서 a태그 추출
    for title in a_tag(string=re.compile('자기소개서')): #자기소개서 제목 추출
        print(title)
        href= a_tag['href']
        print(href)
     
    

'''
for td_article in table.find_all(string=re.compile('자기소개서')):
    for td_article_title in td_article.parent.parent:
        print(td_article_title.a['href'])
'''
