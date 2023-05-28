import mybot
import json
import requests
#import receive_check

def receive_message(msg):
    chat_id = msg['chat']['id']
    chat_title = msg['chat'].get('title', 'personal')
    sender_username = msg['from'].get('username', 'NOUSERNAME')
    sender_fullname = msg['from'].get('first_name', ' ') + ' ' + msg['from'].get('last_name', ' ')
    if 'text' in msg:
        text = msg['text']
        print(f'[{chat_title}:{chat_id}] {sender_fullname}({sender_username}) : {text}')
        return text
    else:
        print(json.dumps(msg, indent=4, ensure_ascii=False))

def get_updates():
    txt = None
    # https://core.telegram.org/bots/api#getupdates
    url = f'https://api.telegram.org/bot{mybot.token}/getUpdates'
    r = requests.get(url)

    if r.ok:
        updates = r.json()['result']

        for u in updates:
            if 'message' in u:
                txt = receive_message(u['message'])
            #print(json.dumps(u, indent=4, ensure_ascii=False))
        while updates:
            last_update_id = updates[-1]['update_id']
            r = requests.get(url, params={'offset' : last_update_id+1})
            if r.ok:
                updates = r.json()['result']
            else:
                break
        if not txt == None: return txt
    else:
        print(f'FAIL : {r.json()}')
