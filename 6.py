# ASSIGNMENT 6
# Login Page Form of PEC Website

import requests
from bs4 import BeautifulSoup

url = "https://pec.edu.in/"  # base URL
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
user_link = soup.select_one('a[href="/user"]')  # form page
if user_link:
    user_url = user_link.get("href")
    user_response = requests.get(f"{url}{user_url}")
    if user_response.status_code == 200:
        user_soup = BeautifulSoup(user_response.content, "html.parser")
        form_elements = user_soup.find_all("input")  # input tags for form
        for element in form_elements:
            element_name = element.get("name")  # name of form element
            if element_name:
                print(f"Element Name: {element_name}")
