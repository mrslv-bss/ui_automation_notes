from selenium.webdriver.common.by import By
import pymssql

search_field_loc = (By.ID, "twotabsearchtextbox")
search_button_loc = (By.ID, "nav-search-submit-button")
cell_loc = (By.XPATH, "//div[@data-component-type='s-search-result']")
conn = pymssql.connect(server='#',
                       user='#',
                       password='#',
                       database='#')
