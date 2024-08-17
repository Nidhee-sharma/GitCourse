import time
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.positive
@allure.title("Open the idrive link and verify the Upgrade button")
@allure.description("Verify that the Upgrade button is displayed")
def test_MiniProject3_VWO():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()
        driver.get("https://www.idrive360.com/enterprise/login")

        # Perform login actions
        user_name = driver.find_element(By.ID, 'username')
        user_name.send_keys('augtest_040823@idrive.com')
        password = driver.find_element(By.ID, 'password')
        password.send_keys("123456")
        sign_in = driver.find_element(By.XPATH, '//button[text()="Sign in"]')
        sign_in.click()

        # Wait until the URL contains the expected path
        WebDriverWait(driver, 15).until(EC.url_contains("/enterprise/account"))

        # Capture and print the current URL for debugging
        current_url = driver.current_url
        print("Current URL:", current_url)

        # Assert that the URL contains the expected substring
        expected_url_substring = "/enterprise/account"
        assert expected_url_substring in current_url, f"URL assertion failed. Expected to contain '{expected_url_substring}', but got '{current_url}'"

        # Wait for the text element to be visible and capture the text
        text_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//h5[@class="id-card-title"]'))
        )

        # Debugging: Check if the element is displayed and its HTML content
        print("Is element displayed?", text_element.is_displayed())
        print("Is element enabled?", text_element.is_enabled())
        print("Element HTML:", text_element.get_attribute('outerHTML'))

        actual_text = text_element.text
        print("Text found:", actual_text)

        # Take a screenshot before assertion
        allure.attach(driver.get_screenshot_as_png(), name="before_assertion_screenshot",
                      attachment_type=AttachmentType.PNG)

        # Assert the text content
        expected_text = 'Your free trial has expired'
        assert actual_text.strip() == expected_text, f"Text assertion failed. Expected '{expected_text}', but got '{actual_text}'"

    finally:
        driver.quit()
