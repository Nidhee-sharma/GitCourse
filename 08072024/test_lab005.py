from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#add capabilities , headless mode, create instace of chrome ,headless , add extensions
#add where is my chrome present



def test_login_vwlogin():
    driver = webdriver.Chrome()
    driver.get("https://vwo.com/")
    driver.rferesh()
    driver.back()
    driver.forward()
    print(driver.page_source)
    driver.close()

