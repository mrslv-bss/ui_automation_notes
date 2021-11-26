from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import helpers
from lib.test_logger import logger
from lib.driver import get_driver
from testdata.test_data import url
from lib.helpers import go_to_page, find_and_click, wait_for_page

contact_us_btn = (By.ID, "contact-link")
sign_in_btn = (By.CLASS_NAME, "login")


def click_on_contact_us():
    wait_for_page(url)
    find_and_click(contact_us_btn)


def click_on_sign_in():
    wait_for_page(url)
    find_and_click(sign_in_btn)


if __name__ == '__main__':
    go_to_page(url)
    click_on_sign_in()
