import requests
from bs4 import BeautifulSoup


url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+ keyword +'&oquery=spdlqj+rpdlatnsdnl&tqi=ibcJMdp0YidssOfbufhsssssskR-476271'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

r =  requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

#elms = soup.select('.basicList_link__JLQJf')

import re
elms = soup.find_all(class_= re.compile('^basicList_title'))

for e in elms:
    title = e.a['title']
    price = e.next_sibling.find(class_=re.compile('^price_num')).string
    print(f'{price} : {title}')



#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div > div.basicList_info_area__TWvzp > div.basicList_title__VfX3c > a