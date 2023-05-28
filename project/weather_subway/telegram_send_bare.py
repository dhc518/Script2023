import mybot
import json
import requests


def send_text(chat_id, text):
    url = f'https://api.telegram.org/bot{mybot.token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.get(url, params=params)
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))
    assert(r.ok)

send_text(-915250754, '안녕하세요 주인님 봇입니다.')
send_text(-915250754, '공지사항입니다.')
