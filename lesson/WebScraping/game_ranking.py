import requests
from bs4 import BeautifulSoup


while category < 6
pc_url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bkJB&pkid=3001&qvt=0&query=PC%EA%B2%8C%EC%9E%84%EB%9E%AD%ED%82%B9'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

r = requests.get(pc_url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
i = 1
    while i < 6:
        print(f'{i}\t', end='')

        elms = soup.select(f'#mflick > div > div > div:nth-child(1) > div:nth-child({i}) > strong > a')
        text_elms = str(elms)
        import re

        text_between_gt_and_lt = re.findall(r'>(.*?)<', text_elms)
        if text_between_gt_and_lt:
            print(text_between_gt_and_lt[0])
        i +=1



