from selenium import webdriver
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "https://courses.letskodeit.com/practice"
browsers_list = ["Chrome"]

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
                        filename='alert_text.txt',
                        filemode='w',
                        level=logging.INFO)
    logging.info("Log file Initialized.")
    return Driver


def check_btn_condition():
    button_status = Driver.find_element(By.XPATH, "//input[@id='displayed-text']").get_attribute("style")
    # print("asd"+button_status)
    if button_status == "display: none;":
        return "Hidden"
    elif button_status == "display: block;":
        return "Showed"
    else:
        return "Default"


if __name__ == '__main__':
    for k in browsers_list:
        initialize(k)
        Driver.get(url)
        Driver.set_window_size(1920, 1080)

        # Alert
        Driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
        popup = Driver.switch_to.alert
        popup_text = popup.text
        time.sleep(1)
        print(popup_text)
        popup.accept()

        # Save alert message
        logging.info(popup_text)

        # Hide/Show button
        print("Current button type is '"+check_btn_condition()+"'")
        Driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
        time.sleep(1)
        print("Current button type is '"+check_btn_condition()+"'")
        Driver.find_element(By.XPATH, "//input[@id='show-textbox']").click()
        time.sleep(1)
        print("Current button type is '"+check_btn_condition()+"'")

        # Hover mouse
        scroll_to_element = ActionChains(Driver)
        elem_scroll = Driver.find_element(By.XPATH, "//button[@id='mousehover']")
        scroll_to_element.move_to_element(elem_scroll)
        elem_scroll.click()
        time.sleep(1)
        Driver.find_element(By.XPATH, "//div[@class='mouse-hover']//a[@href='#top']").click()
        time.sleep(2)

        # Save footer
        dynamic_text = Driver.find_element(By.XPATH, "//p[@class='small dynamic-text jqCopyRight']").text
        logging.info(dynamic_text)
        print(dynamic_text)

        # Sign In
        Driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        time.sleep(2)
        Driver.find_element(By.XPATH, "//input[@name='email' and @class='form-control input-md']").send_keys(
            "IncorrectLogin@gmail.com")
        Driver.find_element(By.XPATH, "//input[@name='password' and @class='form-control input-md']").send_keys(
            "IncorrectPassword123;a")
        Driver.find_element(By.XPATH, "//input[@type='submit' and @tabindex='7']").click()
        time.sleep(1)
        error_msg = Driver.find_element(By.XPATH, "//span[@class='dynamic-text help-block']").text
        print(error_msg)
        logging.info(error_msg)
        time.sleep(2)

        # Tabs
        Driver.execute_script('window.open('');')
        wind1 = Driver.window_handles[0]
        wind2 = Driver.window_handles[1]
        Driver.switch_to.window(wind2)
        Driver.get("https://www.google.com/")

        # Driver.switch_to.window(wind1)
        time.sleep(2)

        Driver.quit()  # close all 2 tabs
