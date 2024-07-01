from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlretrieve
import time


def main():
    browser = set_chrome_driver()

    browser.get("https://www.naver.com")
    element = browser.find_element(By.CLASS_NAME, "search_input")
    element.send_keys("아이스크림")
    element.send_keys(Keys.ENTER)
    time.sleep(2)

    # lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(1) > a
    browser.find_element(
        By.CSS_SELECTOR, "div.api_flicking_wrap >  div:nth-child(1) > a"
    ).click()
    time.sleep(3)

    interval = 3

    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        time.sleep(interval)

        cur_height = browser.execute_script("return document.body.scrollHeight")

        if cur_height == prev_height:
            break
        prev_height = cur_height
    # 스크롤 처음으로 움직이기
    browser.execute_script("window.scrollTo(0,0);")
    time.sleep(7)
    # 작은 이미지들 찾아오기
    imgs = browser.find_elements(By.CSS_SELECTOR, ".mod_vw_thumb img")

    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)

            # 큰이미지
            # //*[@id="main_pack"]/section[1]/div/div/div[1]/div[2]/div[1]/img
            # div.viewer_image img

            img_url = browser.find_element(
                By.CSS_SELECTOR, "div.viewer_image img"
            ).get_attribute("src")
            print(img_url)
            # urlretrieve("다운로드받을 파일 경로", "저장경로")
            urlretrieve(img_url, "./crawl/download/" + str(count) + ".jpg")
            count += 1
        except:
            pass

    time.sleep(6)


def set_chrome_driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


if __name__ == "__main__":
    main()
