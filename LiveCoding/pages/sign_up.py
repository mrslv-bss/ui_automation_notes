from selenium.webdriver.common.by import By
from lib import helpers
from lib.test_logger import logger

timeout = 30

# Locators on Sign in page
inp_email_create = (By.ID, "email_create")
btn_email_create = (By.ID, "SubmitCreate")
error_create_account = (By.ID, "create_account_error")

# Locators on Sign in page
inp_first_name = (By.ID, "customer_firstname")
inp_last_name = (By.ID, "customer_lastname")
inp_email = (By.ID, "email")
inp_password = (By.ID, "passwd")
rdo_mr = (By.ID, "uniform-id_gender1")
rdo_mrs = (By.ID, "uniform-id_gender2")
slct_day = (By.ID, "days")
slct_month = (By.ID, "months")
slct_year = (By.ID, "years")
cbx_newsletter = (By.ID, "uniform-newsletter")
cbx_offers = (By.ID, "optin")
inp_addr_first_name = (By.ID, "firstname")
inp_addr_last_name = (By.ID, "lastname")
inp_addr_company = (By.ID, "company")
inp_addr_address_line_1 = (By.ID, "address1")
inp_addr_address_line_2 = (By.ID, "address2")
inp_addr_city = (By.ID, "city")
slct_addr_state = (By.ID, "id_state")
inp_addr_postal_code = (By.ID, "postcode")
slct_addr_country = (By.ID, "id_country")
inp_addr_additional_information = (By.ID, "other")
inp_addr_home_phone = (By.ID, "phone")
inp_addr_mobile_phone = (By.ID, "phone_mobile")
inp_addr_alias = (By.ID, "alias")
btn_register = (By.ID, "submitAccount")

alert_exists = (By.XPATH, "//div[contains(@class, 'alert')]")


def create_account(email):
    helpers.find_and_send_keys(inp_email_create, email, timeout)
    helpers.find_and_click(btn_email_create, timeout)
    if helpers.find(error_create_account, timeout, should_exist=False):
        message = f"Email address '{email}' already registered!"
        logger(message, error=False)
    else:
        sign_up('first_name')


def sign_up(first_name):
    helpers.find_and_send_keys(inp_first_name, first_name, timeout)
    helpers.find_and_click(btn_register, timeout)
