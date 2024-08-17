import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@pytest.mark.positive
@allure.title("Open the signup url of VWO.com - MiniProject2")
@allure.description("Verify that the clicking on signup button changes")
def test_MiniProject3_VWO():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()  # Correct method name
        driver.get("https://app.vwo.com/#/login")

        anchor_tag_element =(driver.find_element(By.LINK_TEXT,'Start a free trial'))
        #anchor_tag_element = (driver.find_element(By.PARTIAL_LINK_TEXT, 'free trial'))
        anchor_tag_element.click()
        assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    finally:
        driver.quit()





