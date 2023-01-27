from bs4 import BeautifulSoup
import requests
import time

page_url = 'https://ifconfig.me/'

#Функция проверки работы сервера
def server_check(url):
    #Делаем запрос на сайт
    global response
    response = requests.get(url)

    '''Обычное условие. Принты добавил чисто для того чтобы была
    некая имитация работы программы. time.sleep() для той же цели :)'''
    if response.status_code == 200:
        print('*Соединение с сервером установлено*')
        time.sleep(1)
        print('Определяю IP-адрес...')
        return response
    else:
        print('Сервер не отвечает.')
        print('Попробуйте чуть позже.')

        """Добавил возврат строки "Fail" для того чтобы потом можно было не продолжать
        работы программы. Код ниже"""
        return 'Fail'

#Функция парсинга html. Передаем туда объект response из функции проверки сервера
def ip_parse(response):
    page = BeautifulSoup(response.text, 'html.parser')

    ip = f'Ваш IP-адрес: {page}'
    print(ip)


if __name__=='__main__':
    print('***Здравствуйте!***')
    print()
    time.sleep(1)

    site = server_check(page_url)
    #Проверка. Если статус-код от сервера != 200 то работа программы закончится
    if site == 'Fail':
        print("Всего доброго!")
    else:
        time.sleep(2)
        ip_parse(site)


