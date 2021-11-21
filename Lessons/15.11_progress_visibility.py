from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
import time

visibility_btn_loc = "//a[@href='/visibility']"
progress_bar_btn_loc = "//a[@href='/progressbar']"
text_input_btn_loc = "//a[@href='/textinput']"
locators_per_hide = {"REMOVED_BTN_XPATH": "//button[@id='removedButton']",
                     "ZERO_WIDTH_BTN_XPATH": "//button[@id='zeroWidthButton']",
                     "OVERLAPPED_BTN_XPATH": "//button[@id='overlappedButton']",
                     "OPACITY_BTN_XPATH": "//button[@id='transparentButton']",
                     "VISIBILITY_HIDDEN_BTN_XPATH": "//button[@id='invisibleButton']",
                     "DISPLAY_NONE_BTN_XPATH": "//button[@id='notdisplayedButton']",
                     "OFF_SCREEN_BTN_XPATH": "//button[@id='offscreenButton']"}

# Visibility
hide_btn_loc = "//button[@id='hideButton']"
# Progress
start_btn_loc = "//button[@id='startButton']"
stop_btn_loc = "//button[@id='stopButton']"
# Text input
input_btn_name_loc = "MyButtonName"  # Enter here button name
input_loc = "//input[@id='newButtonName']"
change_name_btn_loc = "//button[@id='updatingButton']"

url = "http://www.uitestingplayground.com/"
browsers_list = ["Chrome", "Edge"]


def initialize(browser):
    global Driver
    if browser == "Chrome":
        Driver = webdriver.Chrome(
            r"C:\Users\VOLO GLOBAL\Documents\UI_AUTOMATION\FIRST\chromedriver.exe")
    elif browser == "Edge":
        Driver = webdriver.Edge(
            r"C:\Users\VOLO GLOBAL\Documents\UI_AUTOMATION\FIRST\msedgedriver.exe")
    Driver.implicitly_wait(5)
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S',
                        filename='work.log',
                        filemode='w',
                        level=logging.INFO)
    logging.info("Log file Initialized.")
    return Driver


def visibility():
    logging.info("[1] VISIBILITY")
    Driver.find_element(By.XPATH, visibility_btn_loc).click()

    # # Uncomment to click on Hide button
    # Driver.find_element(By.XPATH, hide_btn_loc).click()

    for curr_loc, value in locators_per_hide.items():
        if Driver.find_element(By.XPATH, value).is_displayed():
            logging.info("Element " + curr_loc + " displayed in " + k)

        # How do I check for buttons when they are not showing, and how do I export this to a log file?
        # else below isn't work

        else:
            logging.warning("Element " + curr_loc + " not displayed in " + k)


def progress():
    logging.info("[2] PROGRESS")
    Driver.find_element(By.XPATH, progress_bar_btn_loc).click()
    Driver.find_element(By.XPATH, start_btn_loc).click()
    time.sleep(2)
    Driver.find_element(By.XPATH, stop_btn_loc).click()
    logging.info("Duration is " + Driver.find_element(By.XPATH, "//p[@id='result' and text()]").text + " in " + k)


def text_input():
    logging.info("[3] TEXT INPUT")
    Driver.find_element(By.XPATH, text_input_btn_loc).click()
    Driver.find_element(By.XPATH, input_loc).send_keys(input_btn_name_loc)
    Driver.find_element(By.XPATH, change_name_btn_loc).click()
    assert Driver.find_element(By.XPATH, change_name_btn_loc).text == str(input_btn_name_loc), logging.error(
        "Incorrect name of button, something wrong!")
    # str() because you can fill 'input_btn_name_loc' by integers
    logging.info("Button successfully changed the name to " + str(input_btn_name_loc) + " in " + k)


if __name__ == '__main__':
    for k in browsers_list:
        initialize(k)
        Driver.get(url)
        Driver.set_window_size(1920, 1080)

        visibility()  # [1] || Visibility
        Driver.back()
        progress()  # [2] || Progress
        Driver.back()
        text_input()  # [3] || Text Input

        Driver.quit()
