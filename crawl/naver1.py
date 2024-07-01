import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


url = "https://openapi.naver.com/v1/search/news.json"

headers = {
    "X-Naver-Client-Id": "3YYxxbE85rfXsRuwwM0K",
    "X-Naver-Client-Secret": "ibFQMzjL7j",
}


r = requests.get(url, headers=headers, params={"query": "파이썬"})

# json 가져오기
data = r.json()
# print(data)
# print(data["items"])
for idx, item in enumerate(data["items"], 1):
    print(idx, item["title"], item["link"])
