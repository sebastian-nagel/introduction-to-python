from time import sleep

from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={'height': 1080, 'width': 1920})
    page = context.new_page()
    page.goto("https://www.bundestag.de/abgeordnete/biografien")
    while True:
        try:
            sleep(3)
            page.click("button:has-text(\"Vor\")")
        except Exception:
            break

with sync_playwright() as p:
    run(p)
