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

#basic locator -ID ,NAME, LINK_TEXT, PARTIAL_LINK_TEXT, TAGNAME
#advance -XPATT, CSS SELEctors
def test_MiniProject4_Katalon():
    driver = webdriver.Chrome()


    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.XPATH,'//*[starts-with(text(),"Mak")]').click()  #//*[normalize-space(text()='Make Appointment')]




