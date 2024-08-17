import time
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.positive
@allure.title("Open the katalon link and verify the URL")
@allure.description("Verify that the Upgrade button is displayed")
def test_MiniProject4_Katalon():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()
        driver.get("https://katalon-demo-cura.herokuapp.com/")

        # Perform login actions
        Make_appointment = driver.find_element(By.XPATH, '//*[text()="Make Appointment"]').click()
        time.sleep(3)
        assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/profile.php#login"
        time.sleep(3)
        user_name= driver.find_element(By.ID,'txt-username')
        user_name.send_keys('John Doe')
        password = driver.find_element(By.ID, 'txt-password')
        password.send_keys("ThisIsNotAPassword")
        sign_in = driver.find_element(By.XPATH, '//button[text()="Login"]')
        sign_in.click()
        time.sleep(3)

        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
        Make_appointment_text =driver.find_element(By.XPATH,'//*[@id="appointment"]/div/div/div/h2')
        Make_appointment_text.text == "Make Appointment"



    finally:
        driver.quit()
