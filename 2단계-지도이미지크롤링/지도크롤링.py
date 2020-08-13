# 네이버지도 url https://map.naver.com/v5
'''
<웹 동작 순서>
1 길찾기 버튼 클릭: a.directions
2 도보 클릭 : a.walk
3 출발지 칸에 입력: input#directionStart0
4 첫번째 장소 클릭: ul li:nth-of-type(1) a div.place_box 중에 list[0]
5 도착지.. : input#directionGoal1
6 도착지 클릭: ul li:nth-of-type(1) a div.place_box 중에 list[0]
7 길찾기 버튼 클릭: button.active
8 프린트 버튼 클릭- 새 창 열기: button.btn_print
9 그림으로 저장(div를 png로): div.print_main_content_overlay

'''
# driver.save_screenshot("screenshot.png")

'''
map_div = driver.find_element_by_css_selector("div.print_main_content_overlay")

element_png = map_div.screenshot_as_png("map.png")
with open("test1.png", "wb") as file:
    file.write(element_png)
'''

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.naver.com/v5")

start = input("출발지: ")
arrive = input("목적지: ")

# 1
search_btn = driver.find_element_by_css_selector("a.directions")
search_btn.click()
time.sleep(1)
# 2 도보
walk_btn = driver.find_element_by_css_selector("a.walk")
walk_btn.click()
time.sleep(1)
# 3
start_search = driver.find_element_by_css_selector("input#directionStart0")
start_search.send_keys(start)
time.sleep(1)
# 4 출발지click
start_list = driver.find_elements_by_css_selector("ul li:nth-of-type(1) a div.place_box")
start_click = start_list[0]
start_click.click()
time.sleep(1)
# 5 목적지
arrive_search = driver.find_element_by_css_selector("input#directionGoal1")
arrive_search.send_keys(arrive)
time.sleep(1)
# 6 click
arrive_list = driver.find_elements_by_css_selector("ul li:nth-of-type(1) a div.place_box")
arrive_click = arrive_list[0]
arrive_click.click()
time.sleep(1)
# 7 길찾기
active_btn = driver.find_element_by_css_selector("button.active")
active_btn.click()
time.sleep(1)

# 8 저장 버튼 클릭- 새 창 열기: button.btn_print
print_btn = driver.find_element_by_css_selector("button.btn_save")
print_btn.click()
time.sleep(10)

'''
# 9 저장
map_div = driver.find_element_by_css_selector("div.print_main_content_overlay")

element_png = map_div.screenshot_as_png("map.png")
'''
###################


'''
# 이미지버튼 : li.lnb2 a
image_button = driver.find_element_by_css_selector("li.lnb2 a")
image_button.click()
time.sleep(10)

photo = driver.find_elements_by_css_selector("div#main_pack div div a img") #컨테이너처럼 받고

for i in range(10):
    photo[i].screenshot(str(i+1)+".png")


'''