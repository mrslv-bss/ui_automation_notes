import pymssql

search_field_loc = ("id", "twotabsearchtextbox")
search_button_loc = ("id", "nav-search-submit-button")
cell_loc = ("xpath", "//div[@data-component-type='s-search-result']")
conn = pymssql.connect(server='sqllearn.volo.local',
                       user='pythonuser',
                       password='cA7BHCrLBEGh4CmZ',
                       database='AdventureWorks2019')
