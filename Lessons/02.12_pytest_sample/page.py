from selenium.webdriver.common.by import By

search_field_loc = (By.ID, "twotabsearchtextbox")
search_button_loc = (By.ID, "nav-search-submit-button")
result_text_loc = (By.XPATH, "//span[contains(text(),'results for')]")
no_results_text_loc = (By.XPATH, "//span[contains(text(), 'No results for')]")
