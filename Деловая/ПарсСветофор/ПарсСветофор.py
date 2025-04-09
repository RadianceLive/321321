import pandas as pd
import requests
from bs4 import BeautifulSoup
# import json
from openpyxl import *
from fake_headers import Headers
# import cloudscraper
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as us
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def parse():
    driver = webdriver.Chrome()
    main_url = ['https://svetoforonline.ru/konditerskie-izdeliya/']
    wb = Workbook()
    file = f'{main_url}.xlsx'
    wb.save('.xlsx')
    wb.save(file)
    xl = pd.ExcelFile(file)
    sheet = wb[xl.sheet_names[0]]
    sheet[f'A1'].value = "Товар"
    sheet[f'B1'].value = "Производитель"
    sheet[f'C1'].value = "Артикул"
    sheet[f'D1'].value = "Вес единицы"
    sheet[f'E1'].value = "В наличии"

    sheet[f'A1'].style = "Headline 2"
    sheet[f'B1'].style = "Headline 2"
    sheet[f'C1'].style = "Headline 2"
    sheet[f'D1'].style = "Headline 2"
    sheet[f'E1'].style = "Headline 2"

    main_url = ['https://svetoforonline.ru/konditerskie-izdeliya/']
    # driver = us.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
    '''
    })
    count = 2
    for url in main_url:
        driver.get(f'{url}/1?skip_geo=1')
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'grey')))
        all_positions = driver.find_element(By.CLASS_NAME, 'grey').text.split('/ ')[1].replace(' ', '').strip()
        pages = (int(all_positions) / 20) + 1
        for p in range(int(pages)):
            data_id = []
            driver.get(f'{url}/{p + 1}?skip_geo=1')
            time.sleep(5)
            carts = driver.find_elements(By.CSS_SELECTOR, 'div[class="relative clear"]')
            # print(carts)

            for cart in carts:
                data_id.append(int(cart.get_attribute('data-id')))
            # driver.get(f'https://t.restaurantguru.com/compare/?ids={data_id}')

            driver.get(f'https://t.restaurantguru.com/compare/?ids={",".join(str(element) for element in data_id)}')
            html = driver.find_element(By.CLASS_NAME, 'center_div').find_element(By.CLASS_NAME,
                                                                                 'open_hours_row').get_attribute(
                'innerHTML')

            print(html)
            # driver.get(f'https://t.restaurantguru.com/compare/?ids={",".join(str(element) for element in data_id)}')
            time.sleep(10)
            for c in range(len(data_id)):
                # print(carts[c].get_attribute("data-id"))
                name = driver.find_element(By.ID, f'td_{data_id[c]}').find_element(By.CSS_SELECTOR,
                                                                                   'a[class="title"]').text
                work = driver.find_element(By.CLASS_NAME, 'center_div').find_element(By.CLASS_NAME,
                                                                                     'open_hours_row').find_elements(
                    By.TAG_NAME, 'td')[c].text
                phone = \
                driver.find_element(By.CLASS_NAME, 'center_div').find_element(By.CLASS_NAME, 'phone_row').find_elements(
                    By.TAG_NAME, 'td')[c].text
                type_res = \
                driver.find_element(By.CLASS_NAME, 'center_div').find_element(By.CLASS_NAME, 'type_row').find_elements(
                    By.TAG_NAME, 'td')[c].text
                print(len(driver.find_element(By.CLASS_NAME, 'center_div').find_element(By.CLASS_NAME,
                                                                                        'type_row').find_elements(
                    By.TAG_NAME, 'td')))
                kitchen = driver.find_element(By.CLASS_NAME, 'center_div').find_element(By.CLASS_NAME,
                                                                                        'cuisine_row').find_elements(
                    By.TAG_NAME, 'td')[c].text
                adress = driver.find_element(By.CLASS_NAME, 'center_div').find_element(By.CLASS_NAME,
                                                                                       'address_row').find_elements(
                    By.TAG_NAME, 'td')[c].text
                country = url.split('-')[1]
                sheet[f'A{count}'].value = 'Нет данных' if country == None else country
                sheet[f'B{count}'].value = 'Нет данных' if type_res == None else type_res
                sheet[f'C{count}'].value = 'Нет данных' if name == None else name
                sheet[f'D{count}'].value = 'Нет данных' if kitchen == None else kitchen
                sheet[f'E{count}'].value = 'Нет данных'
                sheet[f'F{count}'].value = 'Нет данных'

                wb.save('restaurant.xlsx')
                count = count + 1
            # print(f'https://t.restaurantguru.com/compare/?ids={",".join(int(element) for element in data_id)}')
            break
        break
        #     type_rest = cart.find_element(By.CLASS_NAME, 'grey').text.split('/ ')[1].strip()


# import requests

# url = 'https://t.restaurantguru.com/restaurant-Armenia-t1'
# r = requests.get(url).text
# print(r)


parse()

