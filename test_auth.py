import conftest
from pages.LoginPage import LoginPage
import time


def test_successful_login(driver):
    login_page = LoginPage(driver)
    (login_page.open_page(conftest.start_url)
     .enter_email(conftest.email)
     .enter_password(conftest.password)
     .click_login_button())
    time.sleep(2)
    current_url = login_page.get_current_url()
    print("Current URL after login:", current_url)

    assert current_url != conftest.start_url, f"Expected other URL, но but kept {current_url}"

def test_wrong_login(driver):
    login_pageWr = LoginPage(driver)
    (login_pageWr.open_page(conftest.start_url)
     .enter_email(conftest.email)
     .enter_password('wrong')
     .click_login_button())
    time.sleep(2)
    current_url = login_pageWr.get_current_url()
    print("Current URL after login:", current_url)

    assert current_url == conftest.start_url, f"Expected the same URL, but navigated to {current_url}"


