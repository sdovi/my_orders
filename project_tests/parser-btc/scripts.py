import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_coingecko():
    url = 'https://www.coingecko.com/en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим div с классом, содержащим название монеты
    coin_div = soup.find('div', class_='tw-flex tw-flex-col 2lg:tw-flex-row tw-items-start 2lg:tw-items-center')

    # Получаем название монеты
    coin_name = coin_div.find('div', class_='tw-font-semibold').text.strip()

    # Создаем DataFrame
    df = pd.DataFrame({'Название монеты': [coin_name]})

    # Записываем данные в файл Excel
    df.to_excel('coingecko_data.xlsx', index=False)

# Запускаем парсер
parse_coingecko()
