import pytest
from selenium.common import TimeoutException
import conftest
from pages.AIPage import AIPage
import time
import random
from datetime import datetime

def test_asstPageByClicking(logged_in_driver):
    ai_Page = AIPage(logged_in_driver)
    ai_Page.click_buttonAI()
    print("Current URL after login:", logged_in_driver.current_url)
    time.sleep(1)
    assert logged_in_driver.current_url == conftest.url_ai


def test_create_and_check_assistant_Positivecase(logged_in_driver):
    """
        Test for creating an assistant and verifying its existence by name.
        1. Navigates to the assistants page
        2. Creates a new assistant
        3. Verifies that the assistant appears in the list
    """
    ai_page = AIPage(logged_in_driver)
    test_name = f"{conftest.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}" #Unique name

    # 1. Navigate to the assistants page
    ai_page.open_page(conftest.url_ai)
    time.sleep(1)

    try:
        # 2. Adding the Assistant
        ai_page.click_buttonCreate()
        ai_page.enter_text(test_name)
        ai_page.click_buttonCreate()
        time.sleep(2)

        # 3. Retrieving the ID of the created assistant
        assistant_id = ai_page.check_assistant(test_name)
        assert assistant_id is not None, f"Assistant '{test_name}' is not found"
        assert assistant_id.isdigit(), f"Incorrect ID: {assistant_id}"

        print(f"Created assistant: {test_name} (ID: {assistant_id})")

    except TimeoutException as e:
        pytest.fail(f"The test did not complete in time: {str(e)}")
    except Exception as e:
        pytest.fail(f"Error during test execution: {str(e)}")

def test_create_and_check_assistant_nothingcase(logged_in_driver):
    """
    Test for creating an assistant and verifying its existence by name:

    1. Navigate to the assistants page
    2. Create a new assistant with an empty name
    """
    ai_page = AIPage(logged_in_driver)
    test_name = ''

    # 1. Navigate to the assistants page
    ai_page.open_page(conftest.url_ai)
    time.sleep(1)

    try:
        # 2. Adding the Assistant
        ai_page.click_buttonCreate()
        ai_page.enter_text(test_name)
        ai_page.click_buttonCreate()
        time.sleep(2)

        # 3. Retrieving the ID of the created assistant
        assistant_id = ai_page.check_assistant(test_name)
        assert assistant_id is not None, f"Assistant '{test_name}' is not found"
        assert assistant_id.isdigit(), f"Incorrect ID: {assistant_id}"

        print(f"Created assistant: {test_name} (ID: {assistant_id})")

    except TimeoutException as e:
        pytest.fail(f"The test did not complete in time: {str(e)}")
    except Exception as e:
        pytest.fail(f"Error during test execution: {str(e)}")



def test_create_and_check_assistant_Paragrapghcase(logged_in_driver, text_fixture):
    ai_page = AIPage(logged_in_driver)
    # 1. Navigate to the assistants page
    ai_page.open_page(conftest.url_ai)
    time.sleep(1)

    try:
        # 2. Adding the Assistant
        ai_page.click_buttonCreate()
        ai_page.enter_text(text_fixture)
        ai_page.click_buttonCreate()
        time.sleep(2)

        # 3. Retrieving the ID of the created assistant
        assistant_id = ai_page.check_assistant(text_fixture[:20])
        assert assistant_id is not None, f"Ассистент '{text_fixture[:20]}' не найден"
        assert assistant_id.isdigit(), f"Некорректный ID: {assistant_id}"

        print(f"Created assistant: {text_fixture[:20]} (ID: {assistant_id})")

    except TimeoutException as e:
        pytest.fail(f"The test did not complete in time: {str(e)}")
    except Exception as e:
        pytest.fail(f"Error during test execution: {str(e)}")

def test_delete_and_check_assistant(logged_in_driver, text_fixture):
    ai_page = AIPage(logged_in_driver)
    test_name = f"{conftest.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"  # Unique name
    # 1. Navigate to the assistants page
    ai_page.open_page(conftest.url_ai)
    time.sleep(1)

    # try:
        # 2. Adding the Assistant
    ai_page.click_buttonCreate()
    ai_page.enter_text(test_name)
    ai_page.click_buttonCreate()
    time.sleep(2)

    # 3. Verify that the assistant was successfully created
    assistant_id = ai_page.check_assistant(test_name)

    assert assistant_id is not None, f"Ассистент '{test_name}' не найден"
    assert assistant_id.isdigit(), f"Некорректный ID: {assistant_id}"
    print(f"\nFound Assistant: {test_name} (ID: {assistant_id})")

    # 4. Removing assistant
    ai_page.delete_assistant_by_id(assistant_id)
    print(f"Assistant with ID {assistant_id} is deleted")

    time.sleep(2)  # Wait until the deletion is reflected in the UI

    # 5. Confirm the assistant has been successfully removed
    deleted_id = ai_page.check_assistant(test_name)
    assert deleted_id is None, f"Assistant with ID {assistant_id} id not deleted"

    # except Exception as e:
    #     print(f"Ошибка: {e}")
    #     raise
