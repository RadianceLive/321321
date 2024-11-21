import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl import *
import math

file = f'mayak.xlsx'
wb = Workbook()
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
sheet[f'I1'].value = "Цена"
# sheet[f'J1'].value = "Сайт"


sheet[f'A1'].style = "Headline 2"
sheet[f'B1'].style = "Headline 2"
sheet[f'C1'].style = "Headline 2"
sheet[f'D1'].style = "Headline 2"
sheet[f'E1'].style = "Headline 2"
sheet[f'F1'].style = "Headline 2"
sheet[f'G1'].style = "Headline 2"
sheet[f'H1'].style = "Headline 2"
sheet[f'I1'].style = "Headline 2"
count = 2
for p in range(10):
    main_url = f'https://krasnodar.magazinmayak.ru/catalog/produkti/page={p+1};/'
    resp = requests.get(main_url)

    html = resp.content

    soup = BeautifulSoup(html, 'html.parser')
    print(resp.status_code)
    elements = soup.find_all('a', class_='b-common-item__image-link')
    for product in elements:
        print(product.get('href'))
        product_url = product.get('href')
        resp = requests.get(product_url)
        html_prod = resp.content
        soup = BeautifulSoup(html_prod, 'html.parser')
        
        

        # Eбанный состав
        # composition_text = soup.find('h3', string='Анализ состава:').find_previous('p').get_text(strip=True)
        try:
            composition_text = soup.find_all('div', class_='rc-product-detail')[1].find('p').get_text(strip=True)
        except:
            composition_text='none'
        print(composition_text)
        print('              ')
        print('              ')
        print('              ')

        check_energy = soup.find_all('div', class_='rc-product-detail')
        for i in check_energy:
            energy = i.find_all('p')[-1].get_text(strip=True)
            if 'ккал' in energy:
                if ":" in energy:
                    print(f"-------------------------{energy.split(':')[-1]}")
                else:
                    print(f"-------------------------{energy}")
                
                break
        # energy_value = soup.find('h3', text='Энергетическая ценность:').find_next('p').get_text(strip=True)
                
        # Значение из не менее ебанный таблички
        focus = soup.find('span', string='Направленность').find_next('div', class_='b-characteristics-tab__characteristics-value').get_text(strip=True)
        brand = soup.find('span', string='Бренд').find_next('div', class_='b-characteristics-tab__characteristics-value').get_text(strip=True)
        packed = soup.find('span', string='Упаковано').find_next('div', class_='b-characteristics-tab__characteristics-value').get_text(strip=True)
        weight = soup.find('span', string='Вес').find_next('div', class_='b-characteristics-tab__characteristics-value').get_text(strip=True)
        type_of_feed = soup.find('span', string='Тип корма').find_next('div', class_='b-characteristics-tab__characteristics-value').get_text(strip=True)
        title = soup.find('h1', class_='b-title b-title--h1 b-title--card').get_text(strip=True)
        price_element = soup.find('span', class_='b-product-information__price')
        price = price_element.text if price_element else None


        # Подготовка к заносу в экзель(хуевая)
        data = {
            "Название": [title],
            "Направленность": [focus],
            "Бренд": [brand],
            "Упаковано": [packed],
            "Вес": [weight],
            "Тип корма": [type_of_feed],
            "энергетическая ценность": [energy],
            "composition_text":[composition_text]
        }
   
    
        df = pd.DataFrame(data)
        sheet[f'A{count}'].value = title
        sheet[f'B{count}'].value = focus
        sheet[f'C{count}'].value = weight
        sheet[f'D{count}'].value = type_of_feed
        try:
            sheet[f'E{count}'].value = composition_text
        except:
            sheet[f'E{count}'].value = 'None'
            
        sheet[f'F{count}'].value = brand
        sheet[f'G{count}'].value = packed
        sheet[f'H{count}'].value = energy
        sheet[f'I{count}'].value = price
        wb.save(file)
        count =count+1
        # Запись в эксель, но тут не доебаться
        # df.to_excel("output_data.xlsx", index=False)
