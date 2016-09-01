# 네이버 로그인 url = 'https://nid.naver.com/nidlogin.login'

import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

input_id = input('아이디를 입력하세요: ')
input_pwd = getpass.getpass('비밀번호를 입력하세요: ')

login_url = 'https://nid.naver.com/nidlogin.login'
user_id = input_id
user_pwd = input_pwd

driver = webdriver.Chrome('C:/Users/hufs/Downloads/download/lawjmc/chromedriver')  # Optional argument, if not specified will search path.
driver.get(login_url)
driver.find_element_by_id('id').send_keys(user_id)
driver.find_element_by_id('pw').send_keys(user_pwd)

btn = driver.find_element_by_class_name('btn_global')
btn.click()



#driver.close()
