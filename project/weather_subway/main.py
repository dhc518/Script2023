# 입력
# 봇 받기
# 웹 검색 및 저장
# 저장한 내용 봇 보내기

import receive
import receive_check
import scrap

while True:
    txt = receive.get_updates()
    if not txt == None:
        word_list = receive_check.check_text(txt)
        scrap.Scrap(word_list)
        #send





