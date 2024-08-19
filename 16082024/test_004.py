import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
@pytest.mark.positive
@allure.title("Verify that the URL changes when we click on 'Make Appointment'")
@allure.description("Verify that the URL changes when the 'Make Appointment' button is clicked.")
def test_MiniProject1_katalon():
    driver = webdriver.Chrome()


    driver.maximize_window()  # Correct method name
    driver.get("https://the-internet.herokuapp.com/dropdown")
    element_select = driver.find_element(By.ID,"dropdown")
    select = Select(element_select)
    select.select_by_visible_text('Option2')
    time.sleep(5)

    #static -s select class
        #dynamic one can be static and custo control

