from playwright.sync_api import sync_playwright
import time

url = 'https://naver.com'
p = sync_playwright().start()

browser = p.chromium.launch(headless=False).new_context(
    viewport={'width':800, 'height':600}
)

page = browser.new_page()
page.goto(url)
page.get_by_role("link", name="NAVER 로그인").click()
page.get_by_placeholder("아이디").click()
page.get_by_placeholder("아이디").fill("dhc518")
page.get_by_placeholder("아이디").press("Tab")
page.get_by_placeholder("비밀번호").fill("CodeGeass2022#")
page.get_by_placeholder("비밀번호").press("Enter")

time.sleep(10)
