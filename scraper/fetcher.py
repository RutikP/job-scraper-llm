from playwright.sync_api import sync_playwright
from config.settings import CAREERS_URL


def fetch_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(CAREERS_URL, wait_until="networkidle")
        html = page.content()
        browser.close()
    return html


def fetch_job_description(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        browser.close()
    return html
