import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import *
from fake_useragent import UserAgent
import cloudscraper

ua = UserAgent()
#z='bitovaya-himiya-2'
file = f'VetAprKrasnodar.xlsx'
wb = Workbook()
wb.save(file)
xl = pd.ExcelFile(file)
sheet = wb[xl.sheet_names[0]]
count=2
sheet[f'A1'].value = "Наименование"
sheet[f'B1'].value = "Цена"
sheet[f'A1'].style = "Headline 2"
sheet[f'B1'].style = "Headline 2"

for p in range(1, 2):
    scraper = cloudscraper.create_scraper()
    main_url = f'https://www.google.com/search?sa=X&sca_esv=e1f1598d7223311f&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=ADLYWILLYs7XdOpxUgqShdUVC1JxAnHAmw:1717856372328&q=%D0%B7%D0%BE%D0%BE%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD%D1%8B+%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D0%B0&rflfq=1&num=10&ved=2ahUKEwiu6OPWmcyGAxXnKBAIHdPXDYgQjGp6BAgcEAE&biw=1134&bih=738&dpr=1.25#rlfi=hd:;si:;mv:[[45.0780042,39.1259964],[45.011838399999995,38.971197499999995]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:{p};/'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
    resp = scraper.get(main_url)

    html = resp.content
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='rlfl__tls rl_tls')
    products_list = []
    
    for card in cards:
        # Получаем название
         name_tag = card.find('div', class_='dbg0pd')
         name = name_tag.text.strip() if name_tag else None
    
         address_and_phone_div =  card.find_all('div')[2]
         address, phone = address_and_phone_div.split(' · ')
         data = {
            "Название": name,
            "Телефон": phone,
            "Адресс": address,}
         sheet[f'A{count}'].value = data['Название']
         sheet[f'B{count}'].value = data['Телефон']
         sheet[f'C{count}'].value = data['Адрес']
         wb.save(file)
         count=count+1
       