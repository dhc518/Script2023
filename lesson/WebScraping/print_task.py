from playwright.sync_api import sync_playwright
import time

url = 'https://eclass.tukorea.ac.kr/ilos/main/member/login_form.acl'
p = sync_playwright().start()

browser = p.chromium.launch(headless=False).new_context(
    viewport={'width':800, 'height':600}
)

page = browser.new_page()
page.goto(url)

page.locator('input[name="usr_id"]').fill('2019180013')
#page.locatot('#usr_id')
page.locator('input[name="usr_pwd"]').fill('CodeGeass2022#')
page.locator('#login_btn').click()

page.get_by_text("스크립트언어 (04)").click()
time.sleep(1)
page.locator("#submain-contents").get_by_text("과제", exact=True).click()
time.sleep(1)

elms = page.locator('a.site-link').all() # list 로 저장
# e for e in elms if indisight
text_list = [e.text_content() for e in elms]
text_num = len(text_list)
for t in text_list:

    page.get_by_text(t, exact=True).click()
    title = t
    title = title.replace("온라인", "")
    title = title.replace("\n", "")
    print(f'\n\n게시물 번호 : {text_num}')
    text_num -= 1
    print(f'제목 : {title}\n')
    time.sleep(1)
    print('내용 : ')
    for l in page.locator('p').all()[1:-3]:
        print(l.text_content())



    page.goto("https://eclass.tukorea.ac.kr/ilos/st/course/report_list_form.acl")
    time.sleep(1)