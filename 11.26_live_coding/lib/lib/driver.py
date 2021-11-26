from selenium import webdriver


def initialize():
    try:
        return webdriver.Chrome(
            r"C:\Users\VOLO GLOBAL\Documents\UI_AUTOMATION\FIRST\chromedriver.exe")
    except Exception as error:
        raise Exception(error)
