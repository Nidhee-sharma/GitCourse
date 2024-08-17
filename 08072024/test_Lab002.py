import time

from selenium import webdriver

def test_login_vwlogin():
    driver = webdriver.Chrome()
    driver.get("https://vwo.com/")
    print(driver.title)
    time.sleep(10)

    assert driver.title == "login "
    driver.close()
