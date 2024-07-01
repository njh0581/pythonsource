#  파이썬 - 뉴스기사 크롤링
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://news.google.com/search?q=파이썬&hl=ko&gl=KR&ceid=KR%3Ako"
    with requests.Session() as s:
        r = s.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        data_extract(soup)


def data_extract(soup):
    base_url = "https://news.google.com"
    articles = soup.select("div.UW0SDc article")
    for article in articles:
        # print(article)
        link_title = article.select_one("div > div:nth-child(2) a")
        news = []
        news_items = []
        # print(link_title)
        # 제목
        title = link_title.text
        # 뉴스기사 링크 추출
        href = base_url + link_title["href"][1:]
        # 작성자
        writer = article.select_one("div.a7P8l > div").text
        # 작성일자와 시간
        # T기준으로 분리
        report_date_time = article.select_one("time")
        if report_date_time:
            # ['2024-04-19', '07:00:002' ]
            report_date_time = report_date_time["datetime"].split("T")
            report_date = report_date_time[0]
            report_time = report_date_time[1]
        else:
            report_date = ""
            report_time = ""

        print(title, href, writer, report_date, report_time)


if __name__ == "__main__":
    main()
