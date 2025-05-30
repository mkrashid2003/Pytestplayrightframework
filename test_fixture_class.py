import pytest
from playwright.sync_api import sync_playwright

#class will be executed once before all tests in the class.
@pytest.fixture(scope="class")
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        request.cls.browser = browser
        yield browser
        browser.close()
# This fixture sets up a new page in the browser for each test.
#function will be executed after each test function in the class.
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

# This fixture is used to ensure that the browser is set up before any tests in the class are run.

# The `@pytest.mark.usefixtures` decorator is applied to the class to ensure that the `browser` fixture is used for all tests in the class.
@pytest.mark.usefixtures("browser")
class Test_Titleclass:

    def test_google(self, page):
        page.goto("https://www.google.com")
        page.wait_for_timeout(2000)
        assert page.url== "https://www.google.com/"
        page.screenshot(path='./screenshot/google.png')

    def test_orange(self, page):
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_timeout(2000)
        assert page.url== "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        page.screenshot(path='./screenshot/orangehrm.png')

    def test_orange1(self, page):
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_timeout(2000)
        assert page.url== "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        page.screenshot(path='./screenshot/orangehrm1.png')


