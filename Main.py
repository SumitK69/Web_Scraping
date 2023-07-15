from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from Configs import username,password

url = "https://hisabkitab.lse.co.in/Account/Login"

driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.NAME, "UserName").send_keys(username)
driver.find_element(By.NAME, "Password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, ".btn-bordred.btn-custom").click()
print("logged in succesfully")
print("extracting the holdings data.")
holdings = driver.get("https://hisabkitab.lse.co.in/Home/Holding")

driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()

accountids = driver.find_elements(By.CLASS_NAME, "m-t-0")


table_list = []


fetch_tables = driver.find_elements(By.ID, "datatable")

for fetch_table in fetch_tables:
    table_list.append(fetch_table.get_attribute('outerHTML'))


for accountid, table in zip(accountids, table_list):
    df = pd.read_html(table)
    new_df = df[0]
    cols = pd.MultiIndex.from_tuples(new_df.columns)
    multiindexdf = pd.DataFrame(new_df, columns=cols)
    print(accountid.text, "\n")
    print(multiindexdf)
    print("\n \n \n \n")
