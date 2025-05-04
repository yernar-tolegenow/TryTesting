from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_current_url(self):
        return self.driver.current_url

    def open_page(self, url):
        self.driver.get(url)
        return self

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/form/div/div[1]/input'))
        )
        email_field.send_keys(email)
        return self

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/form/div/div[2]/div[1]/input'))
        )
        password_field.send_keys(password)
        return self

    def click_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/form/div/div[3]/button'))
        )
        login_button.click()
        return self

