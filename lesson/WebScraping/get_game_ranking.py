from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
import time

keyword = '네이버 게임순위'
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+ keyword +'&oquery=spdlqj+rpdlatnsdnl&tqi=ibcJMdp0YidssOfbufhsssssskR-476271'

p = sync_playwright().start()
browser = p.chromium.launch(headless=False).new_context(
    user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
)
page = browser.new_page()
page.goto(url)

src_size = 0

while src_size <len(page.content()):
    src_size = len(page.content())
    page.keyboard.press('End')
    time.sleep(1)

soup = BeautifulSoup(page.content(), 'lxml')
elms = soup.find_all(class_=re.compile('^a.text'))

for e in elms:
    title = e.a['title']
    price = e.next_sibling.find(class_=re.compile('^a.strog')).text
    print(f'{price=} : {title}')

browser.close()
p.stop()