from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlretrieve
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    browser = set_chrome_driver()

    url = "https://www.youtube.com/watch?v=HosW0gulISQ"

    browser.get(url)
    time.sleep(2)

    # lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(1) > a
    # browser.find_element(
    #     By.CSS_SELECTOR, "div.api_flicking_wrap >  div:nth-child(1) > a"
    # ).click()
    # time.sleep(3)

    interval = 5

    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.documentElement.scrollHeight")

    while True:
        browser.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight)"
        )

        time.sleep(interval)

        cur_height = browser.execute_script(
            "return document.documentElement.scrollHeight"
        )

        if cur_height == prev_height:
            break
        prev_height = cur_height
    # 스크롤 처음으로 움직이기
    # browser.execute_script("window.scrollTo(0,0);")
    # time.sleep(7)

    # 전체 소스를 BeautifulSoup 담기
    soup = BeautifulSoup(browser.page_source, "lxml")

    # 댓글 사용자의 아이디 미치 코멘트 가져오기
    ids = soup.select("#author-text > span")
    comments = soup.select("#content-text > span")
    # 확인

    ids_list = []
    comments_list = []
    for idx in range(len(ids)):
        # print(ids[idx].text.strip(), comment[idx].text.strip())
        clean_id = ids[idx].text.strip()
        clean_id = clean_id.replace("\n", " ")
        clean_id = clean_id.replace("\t", " ")
        ids_list.append(clean_id)
        clean_comment = comments[idx].text.strip()
        clean_comment = clean_comment.replace("\n", " ")
        clean_comment = clean_comment.replace("\t", " ")

        comments_list.append(clean_comment)

    # 데이터 프레임 생성
    dict_data = {"Id": ids_list, "Comment": comments_list}
    df = pd.DataFrame(dict_data)

    df.to_csv("./crawl/file/youtube.csv", index=False)

    time.sleep(5)


def set_chrome_driver():
    options = ChromeOptions()
    # options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


if __name__ == "__main__":
    main()
