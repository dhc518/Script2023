import receive
import receive_check
import scrap
import send

alert_message = ['잘못 입력하셨습니다.','저장을 잘못 하셨습니다.', '저장된 데이터가 존재하지 않습니다.', '저장 되었습니다.','']
help='[. , ..] : 각각 1,2번에 저장된 날씨 및 지하철정보 보내기\n[오늘,내일,금주] [지역명] : 해당 날짜의 날씨\n[노선명] [역명] : 1시간 이내의 지하철 정보\n[날씨1,2] [지역명] : 지역 저장\n[역1,2] [노선명] [역명]: 노선 및 역 저장'

while True:
    list = receive.get_updates()                                # 봇 받기
    try:
        txt , chat_id = list[0], list[1]
    except TypeError:
        txt = None
    if txt == '/start':
        send.send_text(chat_id, '반갑습니다.\n명령어를 보시려면 !를 입력해주세요.')
    elif txt == '!':
        send.send_text(chat_id, help)
    elif not txt == None:
        word_list = receive_check.check_text(txt, chat_id)      # 분석
        if len(word_list) == 5 and word_list[0] == '오늘':       # 스크랩
            txt = '날씨\n' + scrap.Scrap(word_list[:3])
            txt += '\n\n지하철\n' + scrap.Scrap(word_list[3:])
        elif word_list in alert_message:
            txt = word_list
        else: txt = scrap.Scrap(word_list)

        if txt =='': txt = alert_message[0]
        send.send_text(chat_id, txt)                            # 봇 보내기
        txt = '검색이 종료되었습니다.\n문제가 있으시면,  확인하고 다시 입력해 주세요.'
        send.send_text(chat_id, txt)



