from selenium import webdriver
import logging
from selenium.webdriver.common.by import By

locators = {"BENZ_RADIO_XPATH": "//input[@id='benzradio']",
            "HONDA_CLASS_XPATH": "//option[@value='honda']",
            "ORANGE_MULTIPLE_XPATH": "//option[@value='orange']",
            "PEACH_MULTIPLE_XPATH": "//option[@value='peach']",
            "BENZ_CHECK_XPATH": "//input[@id='benzcheck']",
            "OPEN_TAB_XPATH":
            "//a[@href='https://courses.letskodeit.com/courses']",
            "INPUT_NAME_XPATH": "//input[@name='enter-name']",
            "COURSE_TEXT_XPATH":
            "//td[contains(text(),'Python Programming Language')]",
            "ON_CLICK_XPATH": "//input[@onclick='showElement()']",
            "HIDE_SHOW_XPATH":
            "//input[@placeholder='Hide/Show Example']",
            "MOUSE_HOVER_XPATH":
            "//legend[contains(text(),'Mouse Hover Example')]"}

url = "https://courses.letskodeit.com/practice"
browsers_list = ["Chrome", "Edge"]


def Initialize(browser):
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


if __name__ == "__main__":
  for k in browsers_list:
    Initialize(k)
    Driver.get(url)
    Driver.set_window_size(1920, 1080)
    for curr_loc, value in locators.items():
      if Driver.find_element(By.XPATH, value):
        logging.info("Element "+curr_loc+" founded in "+k)
    Driver.quit()
