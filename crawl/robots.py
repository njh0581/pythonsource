# 크롤링 : 주기적으로 / 무작위로 데이터 수집
# pip install requests  : 웹서버로 요청 시 사용
# pip install beautifulsoup4
# pip install selenium

import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]

file_name = "robots.txt"

for url in urls:
    robots = requests.get(url + file_name)
    print(robots.text)
