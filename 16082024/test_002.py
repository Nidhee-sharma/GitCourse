import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.positive
@allure.title("Verify that the URL changes when we click on 'Make Appointment'")
@allure.description("Verify that the URL changes when the 'Make Appointment' button is clicked.")
def test_MiniProject1_katalon():
    driver = webdriver.Chrome()


    driver.maximize_window()  # Correct method name
    driver.get("https://katalon-demo-cura.herokuapp.com/")

        # Find and click the "Make Appointment" button
    driver.find_element(By.ID, 'btn-make-appointment').click()
    WebDriverWait(driver,10).until(EC.url_contains("profile.php#login"))
        # Verify that the URL has changed to the expected login page
    #expected_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    #assert driver.current_url == expected_url

    user_name = driver.find_element(By.CSS_SELECTOR,'#txt-username').send_keys("John Doe")
    password =driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys("ThisIsNotAPassword")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn-login'))
    )

    driver.find_element(By.CSS_SELECTOR,'#btn-login').click()

    WebDriverWait(driver,5).until(EC.url_contains("#appointment"))

    h2_elemet = driver.find_element(By.XPATH,'//h2[text()="Make Appointment"]')
    allure.attach(driver.get_screenshot_as_png(),name ="H2_login",attachment_type=AttachmentType.PNG)
    assert h2_elemet.text == "Make Appointment"