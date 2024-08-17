import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@pytest.mark.positive
@allure.title("VWO invalid Login page - MiniProject2")
@allure.description("Verify that the invalid name,password and error message")
def test_MiniProject2_VWO():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()  # Correct method name
        driver.get("https://app.vwo.com/#/login")
        assert driver.current_url =="https://app.vwo.com/#/login"

        # Find and click the "Make Appointment" button
        driver.find_element(By.NAME, 'username').send_keys("jjj")
        driver.find_element(By.ID, 'login-password').send_keys("kkk")
        driver.find_element(By.ID,'js-login-btn').click()
        time.sleep(5) #telling python interpreter to stop but we should tell to driver to stop
        element = driver.find_element(By.XPATH,'//div[text()="Your email, password, IP address or location did not match"]')
        assert element.text == "Your email, password, IP address or location did not match"

    finally:
        driver.quit()





