import requests
import telegram_bot


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{telegram_bot.api_key}/sendMessage'
    params = {
        'chat_id' : chat_id,
        'text' : text
    }

    r = requests.get(url, params=params)
    print(r.json())

def get_msg(msg):
    msg_id = msg['message_id']
    chat_id = msg['chat']['id']
    username = msg['from'].get('username','NOUSERNAME') # username 이라는 키가 없으면, NOUSERNAME을 대체값으로 사용.
    text = msg.get('text', '***********************************')
    print(f'{chat_id} : {username} : {text}')
    send_message(chat_id, '그룹방을 통해서 봇이 대신 보냅니다. 두혁찬 입니다.')

# url = f'https://api.telegram.org/bot{telegram_bot.api_key}/getUpdates'
# r = requests.get(url)
# if r.ok:
#     updates = r.json()['result'] # 여러 개의 update 데이터들이 들어온다.
#     print(r.json())
#
#     while updates: # 새로운 업데이트가 있으면
#         for u in updates:
#             if 'message' in u:
#                 get_msg(u['message'])
#                 # print(u)
#                 # chat_id = u['message']['chat']['id']
#                 # send_message(chat_id, '반갑습니다...주인님')
#
#         # 메세지를 다 읽었으면
#
#         last_update_id = updates[-1]['update_id']
#         #print(f'{last_update_id}')
#         params = {'offset' : last_update_id+1}
#         r = requests.get(url, params=params) # 마지막 메시지의 다음부터 새로 업데이트를 읽어온다.
#         updates = r.json()['result'] if r.ok else None # 다음 id로 업데이트
send_message(-961028200,'그룹방을 통해서 봇이 대신 보냅니다. 두혁찬 입니다.')
