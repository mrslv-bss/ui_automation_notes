from selenium.webdriver.common.by import By
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda : 1)) # I use this whole expression instead of simply one __file__ variable because __file__ is deemed less reliable  
parent_dir = os.path.dirname(os.path.dirname(current_path))
if parent_dir not in sys.path: sys.path.append(parent_dir)
if (parent_dir + "\\pages") not in sys.path: sys.path.append(parent_dir + "\\pages")# This is done in order to be able to import modules from POM directory i.e. page objects
from lib import helpers

subject_heading_dropdown = (By.ID, 'id_contact')
email_address_field = (By.ID, 'email')
order_reference_field = (By.ID, 'id_order')
message_textarea = (By.ID, 'message')
submit_button = (By.ID, 'submitMessage')
error_notification = (By.XPATH, '//div[@class="alert alert-danger"]')


def select_subject_heading(optionValue):
    select = helpers.find(subject_heading_dropdown)
    select.select_by_value(optionValue)

def fill_the_email_field(value):
    helpers.find(email_address_field).send_keys(value)

def fill_the_message(message):
    helpers.find(message_textarea).send_keys(message)

def click_submit_button(message):
    helpers.find(submit_button).click()

def get_error_notification_innertext():
    the_text = helpers.find(error_notification).get_attribute("innerText")
    return the_text
