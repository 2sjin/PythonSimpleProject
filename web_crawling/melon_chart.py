# 멜론 TOP100 실시간 차트순위 검색결과 가져오기

from bs4 import BeautifulSoup
import requests

# 헤더('chrome://version'에서 사용자 에이전트 가져오기)
# Response 406 에러 해결하기
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

# URL 접속 후, 페이지 정보 요청하기
url = "https://www.melon.com/chart/index.htm"
r = requests.get(url, headers=headers)

# HTML 분석
html = r.text
soup = BeautifulSoup(html, "html.parser")

# 특정 클래스만 선택(각 클래스명 앞에 '.' 기호 붙이기)
lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
lst = lst50 + lst100

# 특정 클래스 및 자손/자식 태그 선택
for idx, value in enumerate(lst):
    # 순위 출력
    print(f"\n<< {idx+1} >>")

    # 곡명 출력
    title = value.select_one(".ellipsis.rank01 a")
    print("곡명:", title.text)

    # 가수 출력
    # 가수가 2명 이상이면 a 태그가 별개로 존재함
    singers = value.select(".ellipsis.rank02 > a")
    print("가수:", end=" ")
    for singer in singers:
        print(singer.text, end=" ")
    print()
    
    # 앨범 출력
    album = value.select_one(".ellipsis.rank03 > a")
    print("앨범:", album.text)