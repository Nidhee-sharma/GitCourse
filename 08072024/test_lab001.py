from selenium import webdriver

#selenium 4 (selenium manager) who will take care the driver browser
def test_simpleTest():
    driver = webdriver.Edge()
    driver.get("https://www.google.com/")
    assert driver.current_url =='https://www.google.com/'