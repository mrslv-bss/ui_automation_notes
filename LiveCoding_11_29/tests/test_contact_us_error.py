from lib.helpers import find_and_click, go_to_page, find, driver, find_and_send_keys
from testdata.test_data import url, email, order_id, subject_heading
from pages.home import click_on_contact_us
from pages.contact_us import submit_button, error_notification, email_address_field, subject_heading_dropdown, \
    order_reference_field


def main():
    go_to_page(url)
    click_on_contact_us()
    find_and_send_keys(subject_heading_dropdown, subject_heading)
    find_and_send_keys(email_address_field, email)
    find_and_send_keys(order_reference_field, order_id)
    find_and_click(submit_button)
    find(error_notification)
    driver.quit()


if __name__ == '__main__':
    main()
