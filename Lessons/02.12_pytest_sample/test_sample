import pytest
from page import search_field_loc, search_button_loc, result_text_loc, no_results_text_loc
from testdata import url, product


def test_sample(get_driver):
    get_driver.get(url)
    get_driver.maximize_window()
    get_driver.find_element(*search_field_loc).send_keys(product)
    get_driver.find_element(*search_button_loc).click()

    export = get_driver.find_elements(*no_results_text_loc)
    if len(export) <= 0:
        result = get_driver.find_element(*result_text_loc).text
        print(result+" \""+product+"\"")  # pytest -s
    else:
        print("No results")
        raise
    get_driver.close()
