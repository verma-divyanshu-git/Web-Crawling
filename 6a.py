from bs4 import BeautifulSoup
import requests

# Example URL of the form page
url = "https://pec.edu.in/user"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract information from all input elements
    form_inputs = soup.find_all("input")

    # Print the values, names, and placeholders of the input elements
    for input_element in form_inputs:
        input_value = input_element.get("value", "")
        input_name = input_element.get("name", "")
        input_placeholder = input_element.get("placeholder", "")

        print(
            f"Value: {input_value}, Name: {input_name}, Placeholder: {input_placeholder}"
        )

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
