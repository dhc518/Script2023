import mybot
import json
import requests


def send_photo(chat_id, link):
    url = f'https://api.telegram.org/bot{mybot.token}/sendDocument'
    params = {
        'chat_id': chat_id,
        'caption': '사진', # 파일 정보
        'photo': link
    }

    r = requests.get(url, params=params)
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))
    assert(r.ok)


send_photo(-915250754, 'https://i.namu.wiki/i/t6L2WPH9R58UTkIjHDaFo4yj0UDpkG2gYoumm5m63YlJXU3LzeNxcvnZRK7arW3cA2pwFE_2aCl8InjOQQyTbIOpaMwLy6Q4MQFHaC1qStjtQsfoQtgrXZhs_tgSfieS8LZx5RgDJcbsKGqmHsmp2g.webp')
# send_photo(6117047894, 'https://i.namu.wiki/i/t6L2WPH9R58UTkIjHDaFo4yj0UDpkG2gYoumm5m63YlJXU3LzeNxcvnZRK7arW3cA2pwFE_2aCl8InjOQQyTbIOpaMwLy6Q4MQFHaC1qStjtQsfoQtgrXZhs_tgSfieS8LZx5RgDJcbsKGqmHsmp2g.webp')

