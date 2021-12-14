import pytest
from selenium import webdriver
from Helpers.basic import main_page, click, send_keys
from Pages.searched_items_page import choice_item_brand_checkbox
from Pages.main_page import login_register_button_loc, search_field_loc, search_button_loc
from TestData.test_data import word, brand
import time


def test_first(get_driver):
    main_page(get_driver)
    send_keys(get_driver, search_field_loc, word)
    click(get_driver, search_button_loc)
    choice_item_brand_checkbox(get_driver, brand)
    time.sleep(5)
