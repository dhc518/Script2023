from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://eclass.tukorea.ac.kr/ilos/main/member/login_form.acl")
    page.get_by_role("textbox", name="아이디").click()
    page.get_by_role("textbox", name="아이디").fill("2019180013")
    page.get_by_role("textbox", name="아이디").press("Tab")
    page.get_by_role("textbox", name="비밀번호").fill("CodeGeass2022#")
    page.get_by_title("로그인").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)