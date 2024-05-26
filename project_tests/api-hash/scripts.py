import requests
from bs4 import BeautifulSoup

# Настройте данные для входа
phone_number = '+998900856199'

# Создайте сессию
session = requests.Session()

# Шаг 1: Войдите на сайт
auth_url = 'https://my.telegram.org/auth/send_password'
response = session.post(auth_url, data={'phone': phone_number})

if response.status_code == 200:
    print("Введите код, отправленный в Telegram: ")
    code = input()

    # Шаг 2: Подтвердите код
    auth_code_url = 'https://my.telegram.org/auth/login'
    response = session.post(auth_code_url, data={'phone': phone_number, 'random_hash': response.json()['random_hash'], 'password': code})

    if response.status_code == 200:
        print("Успешный вход")

        # Шаг 3: Перейдите на страницу создания приложения
        apps_url = 'https://my.telegram.org/apps'
        response = session.get(apps_url)

        # Вывод содержимого страницы для отладки
        print(response.text)

        if 'Create new application' in response.text:
            # Шаг 4: Заполните и отправьте форму создания приложения
            soup = BeautifulSoup(response.text, 'html.parser')
            hash_input = soup.find('input', {'name': 'hash'}).get('value')

            create_app_url = 'https://my.telegram.org/apps/create'
            app_data = {
                'hash': hash_input,
                'app_title': 'MyApp',
                'app_shortname': 'myapp',
                'app_url': 'https://example.com',
                'app_platform': 'desktop',
                'app_desc': 'Description of my app'
            }

            response = session.post(create_app_url, data=app_data)
            if response.status_code == 200:
                # Шаг 5: Получите API ID и API HASH
                soup = BeautifulSoup(response.text, 'html.parser')
                api_id_element = soup.find_all('span', {'class': 'form-control input-lg'})
                if len(api_id_element) >= 2:
                    api_id = api_id_element[0].text.strip()
                    api_hash = api_id_element[1].text.strip()

                    print('API ID:', api_id)
                    print('API HASH:', api_hash)
                else:
                    print("Не удалось найти элементы API ID и API HASH на странице.")
            else:
                print("Ошибка при создании приложения:", response.status_code)
        else:
            print("Не удалось найти строку 'Create new application' на странице.")
    else:
        print("Ошибка при подтверждении кода:", response.status_code)
else:
    print("Ошибка при отправке номера телефона:", response.status_code)
