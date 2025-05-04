import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.LoginPage import LoginPage


start_url = ""
email = ""
password = ""
url_ai = ''
name = "test"

#Reading the file once during import
with open("3D Dental SOFT.ini", encoding="utf-8") as f:
    text = f.read()

@pytest.fixture(scope="session")
def text_fixture():
    return text

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disk-cache-size=0")
    chrome_options.page_load_strategy = 'eager'

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open_page(start_url) \
        .enter_email(email) \
        .enter_password(password) \
        .click_login_button()

    time.sleep(1)
    return driver
