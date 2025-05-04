from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class AIPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)
        return self

    def click_buttonAI(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'ИИ Ассистенты'))
        )
        button.click()
        return self

    def enter_text(self, name):
        assistant_name = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="ChatBot"]'))
        )
        assistant_name.send_keys(name)
        return self

    def click_buttonCreate(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[normalize-space(text())='Добавить']"))
        )
        for button in buttons:
            try:
                if button.is_displayed() and button.is_enabled():
                    button.click()
                    return self
            except Exception:
                continue
        raise Exception("Button 'Добавить' is not found or not available for clicking")

    def check_assistant(self, name):
        try:
            bot_link = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f'//a[@class="link text-inherit" and contains(text(), "{name}")]')
                )
            )

            # Extract ID from href attribute
            href = bot_link.get_attribute("href")
            bot_id = href.split('/')[-1]  # Last part of URL (e.g., "82")

            return bot_id
        except Exception as e:
            print(f"Не удалось найти ассистента с именем '{name}': {str(e)}")
            return None

    def delete_assistant_by_id(self, assistant_id: str):
        """
        Deletes an assistant by given ID by clicking the trash icon in the corresponding row
        and confirming deletion in the popup window.
        """
        try:
            # Step 1: Find all rows
            rows = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//tr"))
            )

            for row in rows:
                if assistant_id in row.text:
                    # Step 2: Click the trash icon
                    trash_icon = row.find_element(By.XPATH, ".//i[contains(@class, 'ti-trash')]")
                    trash_icon.click()

                    # Step 3: Wait for modal window and confirm deletion
                    confirm_button = self.wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//a[contains(@class, 'btn-danger') and text()='Удалить']"))
                    )
                    confirm_button.click()
                    return True  # Successful deletion

            raise Exception(f"Assistant with ID {assistant_id} is not found")

        except Exception as e:
            raise Exception(f"Error while deleting the assistant: {str(e)}")

