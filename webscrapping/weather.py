import requests
from bs4 import BeautifulSoup

# URL of the weather website you want to scrape
url = 'https://meteofrance.com/'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements containing the weather data
    temperature_element = soup.find('span', {'class': 'temperature'})
    condition_element = soup.find('div', {'class': 'condition'})

    # Extract the data
    temperature = temperature_element.text.strip()
    condition = condition_element.text.strip()

    # Print the weather information
    print(f'Temperature: {temperature}')
    print(f'Condition: {condition}')
else:
    print('Failed to retrieve the webpage.')

