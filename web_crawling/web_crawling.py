from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=blog&query="
keyword = input("검색어를 입력하세요: ")
search_url = base_url + keyword

# URL 정보 가져오기
r = requests.get(search_url)

# HTML 분석
soup = BeautifulSoup(r.text, "html.parser")

# 특정 클래스만 선택(맨 앞/띄어쓰기 -> '.' 기호)
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