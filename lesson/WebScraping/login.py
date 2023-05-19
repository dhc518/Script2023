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
page.get_by_text("강의자료", exact=True).click()
time.sleep(1)

elms = page.locator('.number').all() # list 로 저장
# e for e in elms if indisight
text_list = [e.text_content() for e in elms]

for t in text_list[:3]:
    page.get_by_text(t, exact=True).click()
    time.sleep(1)
    for l in page.locator('a.site-link').all():
        with page.expect_download() as download_info:
            l.click()
        download = download_info.value
        download.save_as('d://download/'+ download.suggested_filename)

    page.goto("https://eclass.tukorea.ac.kr/ilos/st/course/lecture_material_list_form.acl")
    time.sleep(1)