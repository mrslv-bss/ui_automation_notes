from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from golem import actions
from golem.actions import get_browser
from pages.main_locators import search_field_loc, search_button_loc, cell_loc, conn

description = """ Create a program which will search in Amazon any product (e.g., Iphone)​
                    Get the first 10 results’ name and price​
                    Go to DB, create a table and save this information """

tags = []

pages = ['main_locators']


def setup(data):
    pass


def test(data):
    actions.navigate(data.URL)
    actions.send_keys(search_field_loc, data.product)
    actions.click(search_button_loc)
    cursor = conn.cursor()
    cursor.execute("""
                    IF OBJECT_ID('dbo.MYROSLAV_TABLE', 'U') IS NOT NULL
                        DROP TABLE dbo.MYROSLAV_TABLE
                    CREATE TABLE dbo.MYROSLAV_TABLE (
                        price VARCHAR(100),
                        title VARCHAR(300)
                    )
                """)

    for b in range(10):
        element = WebDriverWait(get_browser(), 10).until(
            expected_conditions.visibility_of_all_elements_located(cell_loc))
        element_number = element[b]
        data_asin_element = element_number.get_attribute("data-asin")
        print(data_asin_element)  # Product cell (identifier)

        price_int_loc = ('xpath',
                         f"//div[@data-asin='{data_asin_element}'] "
                         f"//span[@class='a-price-whole']")
        price_dec_loc = ('xpath',
                         f"//div[@data-asin='{data_asin_element}'] "
                         f"//span[@class='a-price-fraction']")
        element_price_int = get_browser().find_elements(*price_int_loc)
        element_price_dec = get_browser().find_elements(*price_dec_loc)
        if len(element_price_dec) == 0:  # Skip, If price is absent
            continue
        price_loc = "$"+element_price_int[0].text \
                    + "."+element_price_dec[0].text
        # Connect integer and decimal parts
        print(price_loc)  # Total price format: $nn.nn

        product_title_loc = ('xpath', f"//div[@data-asin='"
                                       f"{data_asin_element}'] "
                                       f"//span[@class='a-size-base-plus "
                                       f"a-color-base a-text-normal']")
        product_title_element = get_browser().find_element(*product_title_loc)
        product_title = product_title_element.text
        print(product_title)  # Title

        cursor.execute("INSERT INTO dbo.MYROSLAV_TABLE VALUES (%s, %s)",
                       (price_loc, product_title))
        conn.commit()

    cursor.execute("select * from dbo.MYROSLAV_TABLE")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def teardown(data):
    pass
