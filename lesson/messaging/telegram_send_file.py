import mybot
import json
import requests


def send_file(chat_id, fname):
    url = f'https://api.telegram.org/bot{mybot.token}/sendDocument'
    params = {
        'chat_id': chat_id,
        'caption': fname # 파일 정보
    }
    with open(fname, 'rb') as f:
        files = {'document': f}
        r = requests.get(url, params=params, files=files)
        print(json.dumps(r.json(), indent=4, ensure_ascii=False))
        assert(r.ok)

send_file(-915250754, 'Dictionary.pdf')

