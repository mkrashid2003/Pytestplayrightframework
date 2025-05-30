import pytest
from playwright.sync_api import sync_playwright
# module scope means the fixture will be executed once per module
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
#function scope means the fixture will be executed once per test function
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
# The `@pytest.mark.usefixtures` decorator is applied to the class to ensure that the `browser` fixture is used for all tests in the class.
@pytest.mark.parametrize('invalid_username, invalid_password', [
    ('admin', 'admin'),
    ('fhjj', 'gfjj')
])
def test_invalid_login(page, invalid_username, invalid_password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill('input[name="username"]', invalid_username)
    page.fill('input[name="password"]', invalid_password)
    page.click('button[type="submit"]')
    page.wait_for_timeout(3000)
    error_message = page.text_content('//div[@role="alert"]//p')
    assert 'Invalid credentials' in error_message
    page.screenshot(path='./screenshot/testinvalid.png')

# The `@pytest.mark.parametrize` decorator is used to run the test with multiple sets of parameters.
@pytest.mark.parametrize('valid_username, valid_password', [
    ('Admin', 'admin123'),
    ('Admin', 'admin123')
])
def test_valid_login(page, valid_username, valid_password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill('input[name="username"]', valid_username)
    page.fill('input[name="password"]', valid_password)
    page.click('button[type="submit"]')
    page.wait_for_timeout(3000)
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    page.screenshot(path='./screenshot/testvalid.png')
