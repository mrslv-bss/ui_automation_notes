from selenium.webdriver.common.by import By
from selenium import webdriver
from Helpers.basic import send_keys, click, get_text, goods_count
from TestData.test_data import brand
import time


brand_name_field_loc = (By.ID, "Brand")
brand_checkbox_loc = (By.XPATH, "//ul[@aria-labelledby='brandNameFacet'] //a[@tabindex='0']")
count_of_goods_loc = (By.XPATH, "//div[@id='products']//article")
items_found_loc = (By.CLASS_NAME, "Su-z")
add_to_cart_loc = (By.XPATH, "//button[@data-track-value='Add-To-Cart']")
view_bag_loc = (By.CLASS_NAME, "tt-z")
bag_count_loc = (By.XPATH, "//dl[@class='OZ-z']//span")
bag_price_loc = (By.XPATH, "//dl[@class='OZ-z']//dd")


def choice_item_brand_checkbox(get_driver):
    send_keys(get_driver, brand_name_field_loc, brand)
    click(get_driver, brand_checkbox_loc)


def compare_results_count(get_driver):
    result_text = get_text(get_driver, items_found_loc).split()
    assert goods_count(get_driver, count_of_goods_loc) == int(result_text[0])


def add_to_cart(get_driver):
    click(get_driver, (By.XPATH, "//a[@itemprop='url']"))
    click(get_driver, add_to_cart_loc)


def wait_for_changing_result(get_driver):
    actual_text = get_text(get_driver, items_found_loc).split()
    main_count = actual_text[0]
    for k in range(10):
        result_text = get_text(get_driver, items_found_loc).split()
        expected_text = result_text[0]
        if main_count != expected_text:
            return True
        time.sleep(1)
    return False


def compare_bag_count(get_driver):
    add_to_cart(get_driver)
    click(get_driver, view_bag_loc)
    count = list(get_text(get_driver, bag_count_loc))
    price = get_text(get_driver, bag_price_loc).split("$")
    first_count = count[1]
    first_price = price[1]
    expected_result_count = int(first_count) + int(first_count)
    expected_result_price = float(first_price) + float(first_price)
    get_driver.back()
    get_driver.back()
    add_to_cart(get_driver)
    click(get_driver, view_bag_loc)
    count = list(get_text(get_driver, bag_count_loc))
    price = get_text(get_driver, bag_price_loc).split("$")
    second_count = count[1]
    second_price = price[1]
    assert float(second_price) == expected_result_price
    assert int(second_count) == expected_result_count
