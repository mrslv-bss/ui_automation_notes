from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib import helpers
from lib.test_logger import logger
from lib.driver import get_driver
from testdata.test_data import url
from lib.helpers import go_to_page, find_and_click, wait_for_page,find_all

contact_us_btn = (By.ID, "contact-link")
sign_in_btn = (By.CLASS_NAME, "login")
LOCATOR_DRESSES_BUTTON = (By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a[@title="Dresses"]')
LOCATOR_ITEM_NAME = (By.XPATH, '//ul[@class="product_list grid row"]/li//a[@class="product-name"]')
LOCATOR_ITEM_PRICE = (
    By.XPATH, '//ul[@class="product_list grid row"]/li//div[@class="right-block"]//span[@class="price product-price"]')


def click_on_contact_us():
    wait_for_page(url)
    find_and_click(contact_us_btn)


def click_on_sign_in():
    wait_for_page(url)
    find_and_click(sign_in_btn)


def open_dresses():
    find_and_click(LOCATOR_DRESSES_BUTTON)


def get_dress_name_and_price():
    dresses = find_all(LOCATOR_ITEM_NAME)
    prices = find_all(LOCATOR_ITEM_PRICE)
    result = ''
    for i in list(zip([i.text for i in dresses], [i.text for i in prices])):
        result += i[0] + ': ' + i[1] + '\n'
    return result

