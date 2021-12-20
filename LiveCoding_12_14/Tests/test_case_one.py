import pytest
from Helpers.basic import start, login, search_goods
from Pages.searched_items_page import choice_item_brand_checkbox, compare_results_count, wait_for_changing_result


def test_first(get_driver):
    start(get_driver)
    login(get_driver)
    search_goods(get_driver)
    choice_item_brand_checkbox(get_driver)
    assert wait_for_changing_result(get_driver)
    compare_results_count(get_driver)
