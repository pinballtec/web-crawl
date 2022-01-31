import requests
import fake_useragent
from bs4 import BeautifulSoup
import lxml
image_number = 0
'''page number'''
storage_number = 1

link = 'https://zastavok.net/'

"""replacing user_agent in request"""
user_agent = fake_useragent.UserAgent().random
header = {'user-agent': user_agent}

req = requests.get(f'{link}{storage_number}', headers=header).text

"""подключение модуля"""
soup = BeautifulSoup(req, 'lxml')

"""parsing main block"""
main = soup.find('div', class_='block-photo')

"""парсинг подкласса в главном блоке(short_full)"""
first_img = main.find_all('div', class_='short_full')

"""for loop to pars all image elements in first_img block"""
for image in first_img:
    image_link = image.find('a').get('href')  # запрос из самого блока кода с картинкой
    '''значение страницы'''
    download_storage = requests.get(f'{link}{image_link}').text  # запрос на саму старницу с картинкой
    download_soup = BeautifulSoup(download_storage, 'lxml')  # lxml - собственно сам парсер
    """ получение части кода из блока с картинкой """
    download_block = download_soup.find('div', class_='image_data')
    download_data = download_block.find('div', class_='block_down')
    result_link = download_data.find('a').get('href')
    print(result_link)
    '''прямой запрос на картинку с старницы'''
    image_bytes = requests.get(f'{link}{result_link}').content
    """Download and save parsed picture in local file"""
    with open(f'{image_number}.jpg', 'wb') as file:
        file.write(image_bytes)

    image_number += 1
    print(f'{image_number}.jpg was downloaded')