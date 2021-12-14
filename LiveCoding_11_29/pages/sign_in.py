from selenium.webdriver.common.by import By
from lib import helpers

# Locators
sign_in_email_fld = (By.ID, 'email')
sign_im_password_fld = (By.ID, 'passwd')
sign_in_subbmit_btn = (By.ID, 'SubmitLogin')

username = 'test'
password = 'test123456!'


def fill_sign_in():
    helpers.find_and_send_keys(sign_in_email_fld, username)
    helpers.find_and_send_keys(sign_im_password_fld, password)
    helpers.find_and_click(sign_in_subbmit_btn)
