import pytest
from selenium import webdriver


@pytest.fixture
def get_driver():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    yield driver
    driver.quit()
