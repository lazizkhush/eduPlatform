import requests
from bs4 import BeautifulSoup

url = 'https://olx.uz'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

listings = soup.find_all('div', class_='css-1sw7q4x')

for item in listings:
    title = item.find('a', class_='css-1tqlkj0').text
    price = item.find('p', class_='css-1vhm4ri').text
    location = item.find('p', class_='css-1pzx3wn').text
    date_published = item.find('p', class_='css-1uf1vew').text

    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Location: {location}")
    print(f"Date Published: {date_published}")
    print('-' * 50)

