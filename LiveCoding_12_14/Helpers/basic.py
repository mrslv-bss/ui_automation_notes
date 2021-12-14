import pytest
from selenium import webdriver
from TestData.test_data import url


def main_page(get_driver):
    get_driver.get(url)
    get_driver.maximize_window()


def click(get_driver, element):
    get_driver.find_element(*element).click()


def send_keys(get_driver, element, text):
    get_driver.find_element(*element).send_keys(text)
