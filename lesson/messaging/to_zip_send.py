import mybot
import json
import requests
import uuid
import os


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
        file_name = download_photo(msg['photo'])
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




import zipfile

def zip_image():
    # 작업 디렉토리 설정
    working_directory = '.'

    # 이미지 파일 확장자 지정
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    # 압축 파일 이름 지정
    zipfile_name = 'images.zip'

    # 압축 파일 생성
    with zipfile.ZipFile(zipfile_name, 'w') as zip:W
        # 작업 디렉토리 내의 모든 파일 검색
        for root, dirs, files in os.walk(working_directory):
            for file in files:
                # 파일이 이미지 파일인 경우에만 압축에 추가
                if os.path.splitext(file)[1].lower() in image_extensions:
                    # 압축 파일에 파일 추가
                    zip.write(os.path.join(root, file), arcname=file)
    print("Complete Zipping")


#get_updates()
#zip_image()
send_file(-915250754, 'images.zip')





