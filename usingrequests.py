import base64
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from Configs import username, password

url = "https://hisabkitab.lse.co.in/Account/Login"

with requests.session() as s:
    login = s.get(url)
    login_page = bs(login.content, "html.parser")
    token = login_page.find(
        "input", {"name": "__RequestVerificationToken"})["value"]
    all_scripts = login_page.find_all('script')
    for number, script in enumerate(all_scripts):
        if 'CryptoJS.enc.Utf8.parse' in script.text:
            parsekey = script.text[1038:1054]

    def encryption(data, parsekey):
        key = parsekey.encode('utf-8')
        iv = parsekey.encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(
            pad(data.encode('utf-8'), AES.block_size))
        return base64.b64encode(encrypted_data).decode('utf-8')

    login_credentials = {"UserName": encryption(username, parsekey),
                         "Password": encryption(password, parsekey), "__RequestVerificationToken": token}
    s.post(url, login_credentials)
    print("logged in successful")
    holidngs_page = s.get("https://hisabkitab.lse.co.in/Home/Holding")

    user_input = input(
        "Press E for Excel format or W for Web scraping format: ")

    if (user_input.upper() == "E"):

        excel_requests = {
            "AsOnDate": "17/07/2023",
            "AccountID": "",
            "FamilyGroup": "",
            "ScripCode": "",
            "Type": "MEMVAR",
            "ExcelFormatType": "Client+Wise",
            "EXCEL": ""
        }

        excel_response = s.post(
            'https://hisabkitab.lse.co.in/Home/Holding', data=excel_requests)
        print("\n Saving Excel File in local directory.")
        with open("excel_file.xlsx", "wb") as f:
            f.write(excel_response.content)

        df = pd.read_excel("./excel_file.xlsx")
        df = df.fillna("")
        df = df.drop(0)
        print(df.to_string(header=False, index=False))

    elif (user_input.upper() == "W"):
        webview_requests = {
            "AsOnDate": "17/07/2023",
            "AccountID": "",
            "FamilyGroup": "",
            "ScripCode": "",
            "Type": "MEMVAR",
            "ExcelFormatType": "Client+Wise",
        }
        webview_response = s.post(
            'https://hisabkitab.lse.co.in/Home/Holding', data=webview_requests)

        accountids_soup = bs(webview_response.content, 'html.parser')
        accountids = accountids_soup.find_all('h4', {'class': "m-t-0"})

        tables_soup = bs(webview_response.content, 'html.parser')
        tables = tables_soup.find_all('table', {'id': 'datatable'})

        table_list = []

        for table in tables:
            table_list.append(str(table))

        for accountid, table in zip(accountids, table_list):

            df = pd.read_html(table)
            new_df = df[0]
            cols = pd.MultiIndex.from_tuples(new_df.columns)
            individual_table = pd.DataFrame(new_df, columns=cols)
            print("\n", accountid.text, "\n")
            print(individual_table)
            print("\n \n \n \n")
