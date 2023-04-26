# NAVER 지식IN 검색결과 출력

from bs4 import BeautifulSoup
import requests

query = input("검색어 입력: ")
page = int(input("검색 페이지 수: "))

# URL 접속 후, 페이지 정보 요청하기
base_url = f"https://search.naver.com/search.naver?where=kin&sm=tab_jum&query={query}&kin_start="

# 
for p in range(0, page):
    start = 10 * p + 1

    print(f"\n========= Page Start : {p+1} / {page} =========\n")

    page_url = base_url + str(p)

    r = requests.get(page_url)

    # HTML 분석
    html = r.text
    soup = BeautifulSoup(html, "html.parser")

    # 특정 클래스만 선택(각 클래스명 앞에 '.' 기호 붙이기)
    items = soup.select(".api_txt_lines.question_text")

    # 웹 크롤링 결과 출력
    for idx, item in enumerate(items, 1):
        print(f"<< {start+idx-1} >>")
        print(item.text)                    # 태그의 텍스트 출력
        print(f"☞  {item.attrs['href']}\n") # 태그의 링크(href) 출력
        
    print(f"========== Page End : {p+1} / {page} ==========")
