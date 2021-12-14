from selenium.webdriver.common.by import By
from Helpers.basic import send_keys, click

brand_name_field_loc = (By.ID, "Brand")
brand_checkbox_loc = (By.XPATH, "//ul[@aria-labelledby='brandNameFacet'] //a[@tabindex='0']")


def choice_item_brand_checkbox(get_driver, name):
    send_keys(get_driver, brand_name_field_loc, name)
    click(get_driver, brand_checkbox_loc)
