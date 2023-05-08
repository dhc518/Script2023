import mybot
import json
import requests
import uuid


def download_file(doc):
    file_name = doc['file_name']
    file_id = doc['file_id']
    r = requests.get(f'https://api.telegram.org/bot{mybot.token}/getFile',
                     params={'file_id':file_id})
    if r.ok:
        server_file_path = r.json()['result']['file_path']
        r = requests.get(f'https://api.telegram.org/file/bot{mybot.token}/' + server_file_path)
        if r.ok:
            with open(file_name, 'wb')  as wf:
                wf.write(r.content)
        else:
            print(f'Fail : {r.json()}')
    else:
        print(f'Fail : {r.json()}')
    return file_name

def download_photo(photo):
    file_id = photo[-1]['file_id']
    r = requests.get(f'https://api.telegram.org/bot{mybot.token}/getFile', params={'file_id':file_id})
    if r.ok:
        server_file_path = r.json()['result']['file_path']
        file_name = f'img{uuid.uuid4().int}' + os.path.splitext(server_file_path)[-1]
        r = requests.get(f'https://api.telegram.org/file/bot{mybot.token}/' + server_file_path)
        if r.ok:
            with open(file_name, 'wb') as wf:
                wf.write(r.content)
        else:
            print(f'FAIL : {r.json()}')
    else:
        print(f'FAIL : {r.json()}')
    return file_name

def receive_message(msg):
    chat_id = msg['chat']['id']
    chat_title = msg['chat'].get('title', 'personal')
    sender_username = msg['from'].get('username', 'NOUSERNAME')
    sender_fullname = msg['from'].get('first_name', ' ') + ' ' + msg['from'].get('last_name', ' ')
    if 'text' in msg:
        text = msg['text']
        print(f'[{chat_title}:{chat_id}] {sender_fullname}({sender_username}) : {text}')
    elif 'document' in msg:
        print(f'[{chat_title}:{chat_id}] {sender_fullname}({sender_username}) : download file ... ', end='')
        file_name = download_file(msg['document'])
        print(f'"{file_name}" ... Downloading done!')
    elif 'photo' in msg:
        print(f'[{chat_title}:{chat_id}] {sender_fullname}({sender_username}) : download file ... ', end='')
        file_name = download_file(msg['photo'])
        print(f'"{file_name}" ... Downloading done!')

    else:
        print(json.dumps(msg, indent=4, ensure_ascii=False))


def get_updates():
    # https://core.telegram.org/bots/api#getupdates
    url = f'https://api.telegram.org/bot{mybot.token}/getUpdates'
    r = requests.get(url)
    if r.ok:
        updates = r.json()['result']
        for u in updates:
            if 'message' in u:
                receive_message(u['message'])

    else:
        print(f'FAIL : {r.json()}')


get_updates()
