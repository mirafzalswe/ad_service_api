# import requests
# from bs4 import BeautifulSoup
# from models import Ad
# def get_from_link():
#     title = []
#     views = []
#     adi_s = []
#
#     url = 'https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return
#     response = requests.get(url)
#     soup = BeautifulSoup(html_content, 'html.parser')
#     #
#     # adw = soup.find_all('span', class_='views nano-eye-text')
#     # ads = soup.find_all('a', class_="bulletinLink bull-item__self-link auto-shy")
#     # adi = soup.find('tr', class_="bull-list-item-js -exact")
#     adw = soup.find_all('span', class_='views nano-eye-text')
#     ads = soup.find_all('a', class_="bulletinLink bull-item__self-link auto-shy")
#     adi = soup.find('tr', class_="bull-list-item-js -exact")
#
#     for i in range(10):
#         adi.append(adi['data-doc-id'])
#         title.append(ads[i].text)
#         views.append(adw[i].text)
#

import requests
from bs4 import BeautifulSoup
from django.db import transaction
from .models import Ad

import os
from ad_service import settings

def get_from_file():

    file_path = os.path.join(settings.BASE_DIR, 'adv_serv', 'parsing/result3.html')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    soup = BeautifulSoup(html_content, 'html.parser')

    adw = soup.find_all('span', class_='views nano-eye-text')
    ads = soup.find_all('a', class_="bulletinLink bull-item__self-link auto-shy")
    adi = soup.find_all('tr', class_="bull-list-item-js -exact")[:10]
    Ad.objects.all().delete()

    ads_to_save = []

    for i in range(10):
        title = ads[i].text
        views = int(adw[i].text)
        ad_id = int(adi[i]['data-doc-id'])
        author = "админ"

        ad_instance = Ad(
            title=title,
            ad_id=ad_id,
            author=author,
            views=views,
            position=(i + 1)
        )
        ads_to_save.append(ad_instance)

    with transaction.atomic():
        Ad.objects.bulk_create(ads_to_save)

    print(f"Successfully saved {len(ads_to_save)} ads to the database.")
