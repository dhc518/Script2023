import os
import uuid
import requests
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