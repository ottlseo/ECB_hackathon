# https://map.naver.com/v5
'''
<웹 동작 순서>
1 길찾기 버튼 클릭: a.directions
2 출발지 칸에 입력: input#directionStart0
3 첫번째 장소 클릭:
3 도착지.. : input#directionGoal1
4
'''

# 시발 ul li:nth-of-type(1) a div.place_box 중에 list[0]


# driver.save_screenshot("screenshot.png")

'''
element1 = browser.find_element_by_class_name('캡처할 위치의 메인 Html의 class명')

element_png = element1.screenshot_as_png
with open("test1.png", "wb") as file:
    file.write(element_png)
'''

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.naver.com/v5")

start = input("출발지: ")

search_btn = driver.find_element_by_css_selector("a.directions")
search_btn.click()
time.sleep(5)

start_search = driver.find_element_by_css_selector("input#directionStart0")
start_search.send_keys(start)
time.sleep(5)

start_list = driver.find_elements_by_css_selector("ul li:nth-of-type(1) a div.place_box")
start_click = start_list[0]
time.sleep(5)

print(start_click.text)

