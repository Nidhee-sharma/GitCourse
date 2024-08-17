import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@pytest.mark.positive
@allure.title("Verify that the URL changes when we click on 'Make Appointment'")
@allure.description("Verify that the URL changes when the 'Make Appointment' button is clicked.")
def test_MiniProject1_katalon():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()  # Correct method name
        driver.get("https://katalon-demo-cura.herokuapp.com/")

        # Find and click the "Make Appointment" button
        driver.find_element(By.ID, 'btn-make-appointment').click()

        # Verify that the URL has changed to the expected login page
        expected_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
        assert driver.current_url == expected_url, f"URL did not match! Expected: {expected_url}, but got: {driver.current_url}"

    finally:
        driver.quit()  # Ensure the browser is closed even if an error occurs
