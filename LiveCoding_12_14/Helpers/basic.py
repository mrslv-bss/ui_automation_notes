import pytest
from selenium import webdriver
from TestData.test_data import url, word
from Pages.main_page import login_register_button_loc
from Pages.login_page import email_field_loc, password_field_loc, sign_in_button_loc
from credentials import email, password
from Pages.main_page import search_field_loc, search_button_loc


def start(get_driver):
    get_driver.implicitly_wait(5)
    get_driver.get(url)
    get_driver.maximize_window()


def click(get_driver, element):
    get_driver.find_element(*element).click()


def send_keys(get_driver, element, text):
    get_driver.find_element(*element).send_keys(text)


def goods_count(get_driver, element):
    count = get_driver.find_elements(*element)
    return len(count)


def get_text(get_driver, element):
    text = get_driver.find_element(*element).text
    return text


def search_goods(get_driver):
    send_keys(get_driver, search_field_loc, word)
    click(get_driver, search_button_loc)


def login(get_driver):
    get_driver.find_element(*login_register_button_loc).click()
    get_driver.find_element(*email_field_loc).send_keys(email)
    get_driver.find_element(*password_field_loc).send_keys(password)
    get_driver.find_element(*sign_in_button_loc).click()
