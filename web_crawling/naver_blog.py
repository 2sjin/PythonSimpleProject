# NAVER 블로그 검색 결과 출력
# selenium을 함께 쓰는 것이 BeautifulSoap만 쓰는 것 보다는 속도가 느림

from bs4 import BeautifulSoup
from selenium import webdriver
# import requests
import time

base_url = "https://search.naver.com/search.naver?where=blog&query="
keyword = input("검색어를 입력하세요: ")
search_url = base_url + keyword

# 웹드라이버 열기
driver = webdriver.Chrome()

# URL 접속 후, 페이지 정보 요청하기
r = driver.get(search_url)
# r = requests.get(search_url)
time.sleep(3)

# 검색 결과를 스크롤하는 자바스크립트 실행
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# HTML 분석
html = driver.page_source
# html = r.text
soup = BeautifulSoup(html, "html.parser")

# 특정 클래스만 선택(각 클래스명 앞에 '.' 기호 붙이기)
items = soup.select(".total_wrap.api_ani_send")

# 웹 크롤링 결과 출력
for idx, item in enumerate(items, 1):
    print("\n<<", idx, ">>")

    # 광고 여부 확인
    ad = item.select_one(".link_ad")
    if ad:
        print("광고입니다.")
        continue

    # 블로그 제목 출력
    blog_title = item.select_one(".sub_txt.sub_name").text
    print(blog_title)

    # 글 제목, URL 출력
    post_title = item.select_one(".api_txt_lines.total_tit")
    print(post_title.text)
    print(post_title.get("href"))   # URL 없으면 None 리턴
    # print(post_title["href"])     # URL 없으면 예외 발생

# 웹드라이버 닫기
driver.quit()