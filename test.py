import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl import *
import math

file = f'Svetofor.xlsx'
wb = Workbook()
try:
    xl = pd.ExcelFile(file)
except:
    wb.save(file)
    xl = pd.ExcelFile(file)
    sheet = wb[xl.sheet_names[0]]
    sheet[f'A1'].value = "Наименование"
    sheet[f'B1'].value = "Направленность"
    sheet[f'C1'].value = "Вес"
    sheet[f'D1'].value = "Тип корма"
    sheet[f'E1'].value = "Состав"
    sheet[f'F1'].value = "Бренд"
    sheet[f'G1'].value = "Упаковано"
    sheet[f'H1'].value = "Энергетическая ценность"
    # sheet[f'I1'].value = "Телефон"
    # sheet[f'J1'].value = "Сайт"
    

    sheet[f'A1'].style = "Headline 2"
    sheet[f'B1'].style = "Headline 2"
    sheet[f'C1'].style = "Headline 2"
    sheet[f'D1'].style = "Headline 2"
    sheet[f'E1'].style = "Headline 2"
    sheet[f'F1'].style = "Headline 2"
    sheet[f'G1'].style = "Headline 2"
    sheet[f'H1'].style = "Headline 2"
    # sheet[f'I1'].style = "Headline 2"
    # sheet[f'J1'].style = "Headline 2"
    wb.save(file)
try:
    wb = load_workbook(f'4Lapy.xlsx')
    sheet = wb[xl.sheet_names[0]]
except:
    pass
count = len(sheet['A']) + 1
all_rows = len(sheet['A'])

for p in range(9):
    if p==1:
        next
    main_url = f'https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/?section_id=166&sort=popular&page={p+1}.htm'

    resp = requests.get(main_url)

    html = resp.content

    soup = BeautifulSoup(html, 'html.parser')
    print(resp.status_code)
    objects = soup.find_all('div', class_='BNWRitm')
    # print(objects)
    arr_href_item = []
    # переход на каждую карточку товара 
    for item in objects:
        href_item = item.find('a')['href']
        resp_item = requests.get(f'https://svetoforonline.ru{href_item}')
        html_item = resp_item.content
        soup_item = BeautifulSoup(html_item, 'html.parser')
        name = soup_item.find('h1', id='h1text').text # имя карточки
        info_left = [info_item.text for info_item in soup_item.find_all('div', class_='left')]
        info = [info_item.text for info_item in soup_item.find_all('div', class_='right')] # информация, по типу артикул и тд
        print(info_left)
        try:
            index = info_left.index('Производитель:')
            dev = info[index]
        except:
            dev = 'Нет данных'
        try:
            index = info_left.index('Артикул:')
            art = info[index]
        except:
            art = 'Нет данных'
            
        try:
            index = info_left.index('В наличии:')
            sum = info[index]
        except:
            sum = 'Нет данных'
            
        try:
            index = info_left.index('Вес единицы:')
            mas = info[index]
        except:
            mas = 'Нет данных'
            
        image = soup_item.find('div', 'prosmotr_img').find('img')['src']
        print(name)
        print('-------------------------------------------------------')
        print(info[:4])
        arr_href_item.append(item.find('a')['href'])
        sheet[f'A{count}'].value = name
        sheet[f'B{count}'].value = dev
        sheet[f'C{count}'].value = art
        sheet[f'D{count}'].value = mas
        sheet[f'E{count}'].value = sum
        sheet[f'F{count}'].value = f'https://svetoforonline.ru{image}'
        wb.save(file)
        count =count+1



