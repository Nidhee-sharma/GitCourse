from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#add capabilities , headless mode, create instace of chrome ,headless , add extensions
#add where is my chrome present



def test_login_vwlogin():
    chrome_option =Options()
    #chrome_option.add_argument("--incogito")
    chrome_option.add_arguments("--page_load_strategy=none")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://vwo.com/")
    driver.manage_window()

