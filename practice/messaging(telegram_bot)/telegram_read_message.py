import requests
import telegram_bot

url = f'https://api.telegram.org/bot{telegram_bot.api_key}/getUpdates'

r = requests.get(url)
if r.ok:
    updates = r.json()['result'] # 여러 개의 update 데이터들이 들어온다.
    print(r.json())

    while updates: # 새로운 업데이트가 있으면
        for u in updates:
            if 'message' in u:
                print(u)

        last_update_id = updates[-1]['update_id']
        print(f'{last_update_id}')
        params = {'offset' : last_update_id+1}
        r = requests.get(url, params=params) # 마지막 메시지의 다음부터 새로 업데이트를 읽어온다.
        updates = r.json()['result'] if r.ok else None # 다음 id로 업데이트
