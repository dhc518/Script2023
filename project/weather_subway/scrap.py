from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
import time



def get_data(word_list, soup):
    tommorw = False
    txt = ''
    if word_list[0] == '내일' or word_list[0] =='오늘':
        elms = soup.find_all(class_=re.compile('graph_content'))

        if word_list[0] == '오늘':
            for e in elms:
                w_time = e.dt.em.string
                if w_time == '내일':
                    break
                weather = e.dd.i.span.string
                pattern = r'<span class="num">(.*?)<span'
                matches = re.findall(pattern, str(e))
                if matches:
                    degree = matches[0]
                # degree = e.dd.div.div.span.string
                print(f'{w_time} {degree}도 {weather}')
                txt += f'{w_time} {degree}도 {weather}\n'

        else:
            for e in elms:
                w_time = e.dt.em.string
                if w_time =='내일': tommorw = True
                if tommorw == True:
                    if w_time == '모레': break
                    weather = e.dd.i.span.string
                    pattern = r'<span class="num">(.*?)<span'
                    matches = re.findall(pattern, str(e))
                    if matches:
                        degree = matches[0]
                    # degree = e.dd.div.div.span.string
                    print(f'{w_time} {degree}도 {weather}')
                    txt += f'{w_time} {degree}도 {weather}\n'
    elif word_list[0] == '금주':
        date = soup.find_all(class_=re.compile('cell_date'))
        weather = soup.find_all(class_=re.compile('cell_weather'))
        temperature = soup.find_all(class_=re.compile('cell_temperature'))
        i = 0
        for d, w, t in zip(date, weather, temperature):
            day = d.span.span.string
            before_noon = w.span.i.span.string
            target_elements = w.find_all('span', class_='blind')

            if len(target_elements) > 1:
                second_element = target_elements[1]
            after_noon = second_element.string

            pattern = r'</span>(.*?)</span>'
            matches = re.findall(pattern, str(t.span.span))
            if matches:
                low_degree = matches[0]

            pattern = r'</span>(.*?)</span>'
            matches = re.findall(pattern, str(t.select_one('span span.highest')))
            if matches:
                high_degree = matches[0]

            print(f'{day} {low_degree}/{high_degree} {before_noon}/{after_noon}')
            txt += f'{day} {low_degree}/{high_degree} {before_noon}/{after_noon}\n'
            if i == 6: break
            i+=1
    else: # 지하철 스크랩
        if time.localtime().tm_hour < 10:
            hour = '0' + str(time.localtime().tm_hour)
        else: hour = str(time.localtime().tm_hour)
        if time.localtime().tm_min < 10:
            min = '0' + str(time.localtime().tm_min)
        else:
            min = str(time.localtime().tm_min)
        recent_time = hour +':'+ min
        two_hour = int(hour) + 1
        if two_hour < 10:
            two_time = '0' + str(two_hour) +':'+ min
        else: two_time = str(two_hour) +':'+ min

        # recent_time = '05:00'
        # two_time='07:00'
        print(recent_time, two_time)
        if two_time < '07:00':
            two_time = '07:00'

        elms = soup.select('tbody > tr')
        #print(elms)
        for e in elms:
            enter = 0
            try:
                if e.td.get('class') != ['timeline', 'empty'] or ['timeline', 'is_row_span']:
                    s_time1 = e.td.div.div.strong.string
                    if recent_time < s_time1 and two_time > s_time1:
                        last_st1 = e.td.div.find_all('div')[1].find_all('em')[1].string
                        #last_st1 = last_st1
                        #last_st1 = last_st1.string
                        print(f'{s_time1} {last_st1}행')
                        txt += f'{s_time1} {last_st1}행\n'

                if e.find_all('td')[1].get('class') != ['timeline', 'empty'] or ['timeline', 'is_row_span']:
                    #print(e.find_all('td')[1].get('class'))
                    s_time2 = e.find_all('td')[1].div.div.strong.string
                    if recent_time < s_time2 and two_time > s_time2:
                        last_st2 = e.find_all('td')[1].div.find_all('div')[1].find_all('em')[1].string
                        print(f'{s_time2:} {last_st2}행')
                        txt += f'{s_time2:} {last_st2}행\n'
            except AttributeError:
                pass
            except IndexError:
                pass
    return txt


def Scrap(word_list):
    try:
        keyword = word_list[0] +' '+ word_list[1] +' '+ word_list[2]
    except IndexError:
        try:
            keyword = word_list[0] + ' ' + word_list[1]
        except IndexError:
            print('잘못 입력하셨습니다.')
            str = '잘못 입력하셨습니다.'
            return str
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
        time.sleep(0.5)

    soup = BeautifulSoup(page.content(), 'lxml')

    txt = get_data(word_list, soup)

    browser.close()
    p.stop()
    return txt