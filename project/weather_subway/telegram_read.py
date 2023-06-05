import mybot
import json
import requests

def get_updates():
    # https://core.telegram.org/bots/api#getupdates
    url = f'https://api.telegram.org/bot{mybot.token}/getUpdates'
    r = requests.get(url)
    if r.ok:
        updates = r.json()['result']
        for u in updates:
            print(json.dumps(u, indent=4, ensure_ascii=False))
    else:
        print(f'FAIL : {r.json()}')


get_updates()

#get_updates(mybot.ghost_token)

