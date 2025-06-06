import pytest
from playwright.sync_api import sync_playwright

def test_login():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page =  browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        page.screenshot(path='./screenshot/testlogin.png')

        browser.close()



