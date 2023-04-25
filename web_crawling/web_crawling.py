from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요: ")
search_url = base_url + keyword

r = requests.get(search_url)
soup = BeautifulSoup(r.text, "html.parser")
items = soup.select(".api_txt_lines.total_tit")

for idx, item in enumerate(items):
    print(f"{idx}: {item.text}")