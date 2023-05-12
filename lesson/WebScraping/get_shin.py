from bs4 import BeautifulSoup

# f = open('alice.html')
# soup = BeautifulSoup(f,'lxml')
# f.close()
#
# for e in soup.find_all('a'):
#     print(e['href'])

import requests

word = '신라면'
url = f'https://www.google.com/search'
params = {'q':word}
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

r = requests.get(url, params=params, headers=headers)
r.raise_for_status()

soup = BeautifulSoup(r.text, 'lxml')
# for i, e in enumerate(soup.find_all('h3')):
#     print(f'#{i}: {e.string}')
# with open('downloaded.html', 'w', encoding='utf-8') as wf:
#     wf.write(r.text)

elms = soup.select('#search a h3[class="LC20lb MBeuO DKV0Md"]')
for e in elms:
    print(e.get_text(), " : ", e.parent.get('href'))
