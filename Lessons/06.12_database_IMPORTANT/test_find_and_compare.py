import pytest
from page import search_field_loc, search_button_loc, full_result_by_title_loc, full_price_list_loc
from testdata import url, product
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def test_sample(get_driver):
    get_driver.get(url)
    get_driver.maximize_window()
    get_driver.find_element(*search_field_loc).send_keys(product)
    get_driver.find_element(*search_button_loc).click()

    for b in range(10):
        element = WebDriverWait(get_driver, 10).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))
        element_number = element[b]
        data_asin_element = element_number.get_attribute("data-asin")
        print(data_asin_element)
        price_int_loc = f"//div[@data-asin='{data_asin_element}'] //span[@class='a-price-whole']"
        price_dec_loc = f"//div[@data-asin='{data_asin_element}'] //span[@class='a-price-fraction']"
        element_price_int = get_driver.find_elements(By.XPATH, price_int_loc)
        element_price_dec = get_driver.find_elements(By.XPATH, price_dec_loc)
        if len(element_price_dec) == 0:
            continue
        price_loc = "$"+element_price_int[0].text+"."+element_price_dec[0].text
        print(price_loc)
    get_driver.close()
