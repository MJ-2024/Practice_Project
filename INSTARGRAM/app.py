from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 파이썬에서 셀레니움을 쓰겠다는 뜻  (모듈 import)
# 셀레니움을 사용하는 이유 : 좀 더 활용성,다이나믹한 사이트들을 크롤링해서 쉽게 분석 할 수 있음


import time
import urllib.request 

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 브라우저 자동 꺼짐 방지 옵션

driver = webdriver.Chrome(options=chrome_options) 
# 크롬 드라이버 생성
driver.implicitly_wait(5) 
# 로딩 딜레이 설정
driver.get('https://instagram.com') 
# driver라는 변수에 원하는 사이트의 모든 정보가 담게됨
# 원하는 사이트 접속&이동

# 원하는 요소들 찾기
# A = driver.find_element(By.CSS_SELECTOR,'._aa4u').text 
# # 클래스 명이 하나에 여러개 포함되어있는경우 하나만 써도 가능
# print(A)

# 인스타그램 로그인
a= driver.find_element(By.CSS_SELECTOR,'input[name="username"]')
a.send_keys('min.jiiim') 
a= driver.find_element(By.CSS_SELECTOR,'input[name="password"]')
a.send_keys('qpalsk109!')
a.send_keys(Keys.ENTER)
driver.implicitly_wait(15)

# 페이지이동 = 사과라는 태그를 검생한 페이지
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/') 
# 첫째사진누름
driver.implicitly_wait(10)
a= driver.find_element(By.CSS_SELECTOR,'._aagw')
driver.execute_script("arguments[0].click();", a)
# 사진저장
driver.implicitly_wait(10)
이미지= driver.find_element(By.CSS_SELECTOR,'._aagv .x5yr21d').get_attribute('src')
urllib.request.urlretrieve(이미지,'0.jpg')
# 다음 버튼
driver.implicitly_wait(10)
next= driver.find_elements(By.CSS_SELECTOR,'._abl-')[0].click()
# 사진저장-다음버튼 반복문을 사용해 자동화 
try:
    for i in range(1,16) :
    # 사진저장
        이미지= driver.find_element(By.CSS_SELECTOR,'._aagv .x5yr21d').get_attribute('src')
        urllib.request.urlretrieve(이미지,str(f'{i}.jpg'))
    # 다음 버튼
        next= driver.find_elements(By.CSS_SELECTOR,'._abl-')[1].click()
        print('다음')
except:
    next= driver.find_elements(By.CSS_SELECTOR,'._abl-')[1].click()



