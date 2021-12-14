from pages.home import open_dresses, get_dress_name_and_price
from lib.helpers import driver, go_to_page, write_to_file
import os


def test(path_to_result_file):
    go_to_page('http://automationpractice.com')
    open_dresses()
    result = get_dress_name_and_price()
    write_to_file(path_to_result_file, result)


if __name__ == '__main__':
    try:
        test(os.path.join(os.path.dirname(__file__), '..', 'testdata', 'result.txt'))
    except Exception as e:
        driver.quit()
        raise e
    driver.quit()
