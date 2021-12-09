import pytest
from page import search_field_loc, search_button_loc, cell_loc
from testdata import url, product
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def test_find_and_compare(get_driver):
    get_driver.get(url)
    get_driver.maximize_window()
    get_driver.find_element(*search_field_loc).send_keys(product)
    get_driver.find_element(*search_button_loc).click()

    for b in range(10):
        element = WebDriverWait(get_driver, 10).until(expected_conditions.visibility_of_all_elements_located(cell_loc))
        element_number = element[b]
        data_asin_element = element_number.get_attribute("data-asin")
        print(data_asin_element) # Product cell code

        price_int_loc = (By.XPATH, f"//div[@data-asin='{data_asin_element}'] //span[@class='a-price-whole']")
        price_dec_loc = (By.XPATH, f"//div[@data-asin='{data_asin_element}'] //span[@class='a-price-fraction']")
        element_price_int = get_driver.find_elements(*price_int_loc)
        element_price_dec = get_driver.find_elements(*price_dec_loc)
        if len(element_price_dec) == 0: # Skip, If price is absent
            continue
        price_loc = "$"+element_price_int[0].text+"."+element_price_dec[0].text # Connect integer and decimal parts
        print(price_loc)
