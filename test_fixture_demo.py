import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    # browser_type_launch is provided by pytest-playwright
    # and already runs outside an asyncio loop
    with sync_playwright() as p:
        browser =  p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page =  browser.new_page()
    yield page
    page.close()

def test_goto_google(page):
    page.goto("https://www.google.com")
    page.wait_for_timeout(2000)
    assert page.title() == "Google"
    page.screenshot(path='./screenshot/testgoogle.png')


def test_goto_redbus(page):
    page.goto("https://www.redbus.in/")
    page.wait_for_timeout(2000)
    assert page.title() == (
        "Bus Ticket Booking Online at Cheapest Price with Top Bus Operators- redBus"
    )
    page.screenshot(path='./screenshot/testredbus.png')

