from selenium import webdriver


def initialize():
    global driver
    driver = webdriver.Chrome(
            r"C:\Users\VOLO GLOBAL\Documents\UI_AUTOMATION\FIRST\chromedriver.exe")
    driver.implicitly_wait(5)
    return driver
