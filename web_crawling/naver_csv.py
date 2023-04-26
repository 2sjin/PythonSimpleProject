import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

FILE_PATH = "web_crawling/csv"

keyword = input("검색어를 입력하세요: ")
url = "https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query=" + quote_plus(keyword)    # 키워드 인코딩

# URL 접속 후, 페이지 읽기
html = urlopen(url).read()

# HTML 분석
soup = BeautifulSoup(html, "html.parser")

# 특정 클래스만 선택(각 클래스명 앞에 '.' 기호 붙이기)
total = soup.select(".api_txt_lines.total_tit")
search_list = []

# [글제목, 링크]를 search_list에 추가
for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    search_list.append(temp)

# search_list를 csv 파일로 저장
f = open(f"{FILE_PATH}/{keyword}.csv", "w", encoding="utf-8", newline="")
csv_writer = csv.writer(f)
for i in search_list:
    csv_writer.writerow(i)

f.close()
print("CSV 파일 저장 완료")