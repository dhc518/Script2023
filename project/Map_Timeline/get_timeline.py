import requests
from bs4 import BeautifulSoup

# Google Takeout 웹 사이트 URL
url = "https://takeout.google.com/settings/takeout/custom/location_history"

# 앱 비밀번호
import app_pass

app_password = app_pass.passwd

# 로그인 세션 만들기
session = requests.session()
session.auth = ("dhc000518@gmail.com", app_password)

# 데이터 다운로드 URL 가져오기
response = session.get(url)
soup = BeautifulSoup(response.text, "html.parser")
download_url = soup.find("a", {"id": "uc-download-link"})["href"]

# 데이터 다운로드
response = session.get(download_url)
with open("Location History.zip", "wb") as f:
    f.write(response.content)

