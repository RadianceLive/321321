import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import *
from fake_useragent import UserAgent
ua = UserAgent()
#z='bitovaya-himiya-2'
file = f'mayak-{z}.xlsx'
wb = Workbook()
wb.save(file)
xl = pd.ExcelFile(file)
sheet = wb[xl.sheet_names[0]]
count=2
sheet[f'A1'].value = "Наименование"
sheet[f'B1'].value = "Цена"
sheet[f'A1'].style = "Headline 2"
sheet[f'B1'].style = "Headline 2"

for p in range(2, 13):
    main_url = f'https://stavropol.magazinmayak.ru/catalog/{z}/page={p};/'
#     headers = {
#     'Cookie': '_ym_uid=1705321650743312540; _ym_d=1705321650; PHPSESSID=c34e2fadd04170806689509a14092858; _ym_isad=1; XQgOdM=vWKesqkjbGyxnQXIMAtlNuaoRCHUhP; vWKesqkjbGyxnQXIMAtlNuaoRCHUhP=b5316aa136b8bfa95035b12facf89c62-1712180896; _ym_visorc=w; XQgOdM_hits=22',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
# }
    resp = requests.get(main_url,headers=headers)

    html = resp.content
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='card-product__body')
    products_list = []
    for card in cards:
        title = str(card.find('a', class_='card-product__title').get('title'))
        price = card.find('div', class_='card-product__price').find('div').text  # предполагается, что цена - это второй элемент после "Цена"
        print({'Название': title, 'Цена': price})
        data = {
            "Название": title,
            "Цена": price,}
        sheet[f'A{count}'].value = data['Название']
        sheet[f'B{count}'].value = data['Цена']
        wb.save(file)
        count=count+1
       