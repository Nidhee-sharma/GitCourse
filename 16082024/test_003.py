import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
@pytest.mark.positive
@allure.title("Open the signup url of VWO.com - MiniProject2")
@allure.description("Verify that the clicking on signup button changes")
def test_MiniProject3_VWO():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(5)
    driver.maximize_window()  # Correct method name
    driver.get("https://app.vwo.com")
    email_input = driver.find_element(By.ID,'login-username').send_keys("admin@gmail.com")
    Pwd_input = driver.find_element(By.ID, 'login-password').send_keys("admin1")
    button = driver.find_element(By.ID,'js-login-btn').click()

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    element = WebDriverWait(driver = driver,poll_frequency=1,timeout= 5,ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    )
    error_message = driver.find_element(By.ID,'js-notification-box-msg').text
    print(error_message)
    assert error_message == "Your email, password, IP address or location did not match"
