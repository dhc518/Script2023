from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
import time

keyword = '신라면'
url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery='+keyword+'&pagingIndex=1&pagingSize=10&productSet=total&query='+keyword+'&sort=price_asc&timestamp=&viewType=list'

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
elms = soup.find_all(class_=re.compile('^basicList_title'))

for e in elms:
    title = e.a['title']
    price = e.next_sibling.find(class_=re.compile('^price_num')).text
    print(f'{price=} : {title}')

browser.close()
p.stop()

