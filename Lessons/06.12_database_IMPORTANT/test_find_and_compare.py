import pytest
from page import search_field_loc, search_button_loc, cell_loc, conn
from testdata import url, product
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def test_find_and_compare(get_driver):
    get_driver.get(url)
    get_driver.maximize_window()
    get_driver.find_element(*search_field_loc).send_keys(product)
    get_driver.find_element(*search_button_loc).click()

    cursor = conn.cursor()
    cursor.execute("""
                    IF OBJECT_ID('dbo.MYROSLAV_TABLE', 'U') IS NOT NULL
                        DROP TABLE dbo.MYROSLAV_TABLE
                    CREATE TABLE dbo.MYROSLAV_TABLE (
                        price VARCHAR(100),
                        title VARCHAR(1000)
                    )
                """)

    for b in range(10):
        element = WebDriverWait(get_driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(cell_loc))
        element_number = element[b]
        data_asin_element = element_number.get_attribute("data-asin")
        print(data_asin_element)  # Product cell (identifier)

        price_int_loc = (By.XPATH,
                         f"//div[@data-asin='{data_asin_element}'] "
                         f"//span[@class='a-price-whole']")
        price_dec_loc = (By.XPATH,
                         f"//div[@data-asin='{data_asin_element}'] "
                         f"//span[@class='a-price-fraction']")
        element_price_int = get_driver.find_elements(*price_int_loc)
        element_price_dec = get_driver.find_elements(*price_dec_loc)
        if len(element_price_dec) == 0:  # Skip, If price is absent
            continue
        price_loc = "$"+element_price_int[0].text \
                    + "."+element_price_dec[0].text
        # Connect integer and decimal parts
        print(price_loc)  # Total price format: $nn.nn

        product_title_loc = (By.XPATH, f"//div[@data-asin='"
                                       f"{data_asin_element}'] "
                                       f"//span[@class='a-size-base-plus "
                                       f"a-color-base a-text-normal']")
        product_title_element = get_driver.find_element(*product_title_loc)
        product_title = product_title_element.text
        print(product_title)  # Title

        cursor.execute("INSERT INTO dbo.MYROSLAV_TABLE VALUES (%s, %s)",
                       (price_loc, product_title))
        conn.commit()

    cursor.execute("select * from dbo.MYROSLAV_TABLE")
    rows = cursor.fetchall()
    for row in rows:
        print(row)  # Show result (pytest -s)

    get_driver.close()
