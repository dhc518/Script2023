import mybot
import json
import requests

def get_updates():
    url = f'https://api.telegram.org/bot{mybot.token}/getUpdates'
    r = requests.get(url)
    if r.ok:
        updates = r.json()['result']
        while updates:
            for u in updates:
                print(json.dumps(u, indent=4, ensure_ascii=False))
            last_update_id = updates[-1]['update_id']
            r = requests.get(url, params={'offset' : last_update_id+1})
            if r.ok:
                updates = r.json()['result']
            else:
                break


get_updates()


# get_updates(mybot.ghost_token)



