import requests
import telegram_bot

def get_msg(msg):
    sender_id = msg['from']['id']
    #sender_username = msg['from']['username']
    sender_fullname = msg['from']['first_name'] + ' ' + msg['from']['last_name']
    if 'text' in msg:
        text = msg['text']
        #print(f'{sender_fullname}({sender_username}:{sender_id}) : {text}')
        print(f'{sender_fullname}({sender_id}) : {text}')

url = f'https://api.telegram.org/bot{telegram_bot.api_key}/getUpdates'
r = requests.get(url)

if r.ok:
    updates = r.json()['result']# list of dictionary
    for u in updates:
        get_msg(u['message'])

if updates:
    last_update_id = updates[-1]['update_id']
    params = {
    'offset': last_update_id + 1
    }
    r = requests.get(url, params=params)