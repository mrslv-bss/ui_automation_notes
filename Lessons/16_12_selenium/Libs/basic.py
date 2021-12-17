from selenium import webdriver
from Libs.driver import initialize
from testdata.testdata import url
from selenium.webdriver.common.by import By
from testdata.testdata import word


driver = initialize()

def start():
    driver.get(url)
    driver.maximize_window()

def sendkeys(element, word):
    driver.find_element(*element).send_keys(word)

def click(element, wait_for):
    driver.find_element(*element).click()
    driver.find_element(*wait_for).is_displayed()

def check_inputted(element):
    res = driver.find_element(*element)
    atr = res.get_attribute("value")
    return atr

def get_result(element):
    result = driver.find_elements(*element)
    return result

def check_word_title():
    for k in range(9):
        title_result_loc = (By.XPATH, f"//div[@id='r1-{k}'] \
            //a[@data-testid='result-title-a']")
        res = driver.find_element(*title_result_loc).text
        x = res.split()
        for i in x:
            if i == word:
                return True
    return False
        

def end():
    driver.quit()
