import pytest
from Helpers.basic import start, login, search_goods
from Pages.searched_items_page import choice_item_brand_checkbox, compare_results_count, add_to_cart, compare_bag_count
import time


def test_first(get_driver):
    start(get_driver)
    login(get_driver)
    search_goods(get_driver)
    choice_item_brand_checkbox(get_driver)
    time.sleep(5)
    compare_results_count(get_driver)
