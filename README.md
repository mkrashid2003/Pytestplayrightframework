# Pytest Playwright Framework

This project demonstrates browser automation testing using [Playwright](https://playwright.dev/python/) with [Pytest](https://docs.pytest.org/).

## Features

- Playwright sync API for browser automation
- Pytest fixtures for browser and page management
- Parametrized login tests (valid/invalid credentials)
- Screenshot capture on test runs

## Project Structure

- `test_chromebrowser.py`: Basic login test
- `test_fixture_demo.py`: Tests using fixtures
- `test_fixture_class.py`: Class-based tests with fixtures
- `data1.py`: Parametrized login tests

## Configuration & Installation

1. **Clone the repository**
 git clone https://github.com/mkrashid2003/Pytestplayrightframework.git
 cd Pytestplayrightframework
2. **Create a virtual environment**
   python -m venv .venv
3. **Activate the virtual environment**
   .venv\Scripts\activate
4. **Install dependencies**
   pip install pytest playwright
5. **Install Playwright browsers**
   playwright install
6.**Install Pytest-html**
pip install pytest-html
## Running Tests

- Run all tests:
  pytest
- Run a specific test file:
  pytest test_fixture_demo.py
- Run your tests with HTML report output:
  pytest --html=report.html


7. 
