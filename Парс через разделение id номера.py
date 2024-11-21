import pandas as pd
from bs4 import BeautifulSoup

# Функция для извлечения данных из HTML фрагмента
def extract_data_from_html(html_fragment):
    soup = BeautifulSoup(html_fragment, 'html.parser')
    companies = []
    
    for company in soup.find_all('div', class_='companies__item', itemprop="itemListElement"):
        name_elem = company.find('a', class_='companies__item-title-text')
        get_id = name_elem.get('href').split('/')[-2].split('_')[-1]
        print(get_id)
        address_elem = company.find('div', class_='companies__item-address')
        phone = company.find('span', {"ng-show" :(f'isFullPhone{get_id}')}).get_text(strip=True) if company.find('span', {"ng-show" :(f'isFullPhone{get_id}')}) != None else 'Не указан'
        name = name_elem.get_text(strip=True) if name_elem else 'Не указано'
        address = address_elem.get_text(strip=True) if address_elem else 'Не указан'


        companies.append({
            'Название': name,
            'Адрес': address,
            'Телефон': phone
        })
    
    return companies

# Основная функция для обработки нескольких HTML фрагментов и сохранения их в Excel
def process_html_fragments(html_fragments, output_path):
    all_companies = []
    
    for html_fragment in html_fragments:
        companies = extract_data_from_html(html_fragment)
        all_companies.extend(companies)
    
    df = pd.DataFrame(all_companies)
    df.to_excel(output_path, index=False)
    print(f"Данные успешно сохранены в файл {output_path}")

# Пример использования
html_fragments = [
    """
   <div itemscope="" itemtype="http://schema.org/ItemList">
    
<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/veterinarnaya-klinika-bolshaya-medveditsa_10193908/">
                            <img src="https://image2.yell.ru/imager/NzM1ZWViMDg2MjkyNDc0YzA5M/170x170/responses/2/1/7/r_1661435_12656_xb11v4890c6g55p5_1624456409.jpg" alt="Ветеринарная клиника Большая Медведица" style="opacity: 1; transition: all 0.5s ease 0s;">
                                        <img class="companies__item-badge" src="/img/yell_badge/yell_badge_2024.png" alt="">
                    </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-green">
                        Открыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">1.</span>
                                        <meta itemprop="position" content="1">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/veterinarnaya-klinika-bolshaya-medveditsa_10193908/" itemprop="url">
                        Ветеринарная клиника Большая Медведица                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул им Маяковского, д 150                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.4    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 88%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/veterinarnaya-klinika-bolshaya-medveditsa_10193908/reviews/"><span>250</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/veterinarnye-kliniki/">Ветеринарные клиники</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 3                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Ветеринарные аптеки                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    <a href="/krasnodar/top/salony-dlya-zhivotnykh/">Салоны для животных</a>                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                        <div class="companies__item-offer">
                            <a class="is-relative" href="/krasnodar/events/953001/">
                                                                                                до&nbsp;31 июля 2024 —
                                 Курьерская доставка медикаментов для животных                                                        </a>
                        </div>
                    </div>
                                        <div class="companies__contact">
                                            <div class="button button_size_xxs button_theme_red company_short_button_phone_premium" ng-click="isFullPhone10193908 = true;">
                            <span class="ng-hide" ng-show="isFullPhone10193908">8 (901) 246-19-67</span>
                            <span ng-hide="isFullPhone10193908" class="company_short_button_phone_premium">8 (901) 246-19... — показать</span>
                        </div>
                                                                </div>
                </div>
                </div>
                                            <div class="companies__item-price">
                    <div class="price">
                        <div class="price__list">
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Услуги специалистов</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 700 руб.</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Вакцинация собак</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 1050 руб.</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Вакцинация кошек</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 1010 руб.</span>
                                </span>
                            </div>
                                                </div>
                    </div>
                                    </div>
                        </div>
            <div>
                    <div class="companies__item-review            ">
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-bolshaya-medveditsa_10193908/?reviewId=4762576">
                «Наблюдаемся с нашей собакой у Екатерины Николаевны, с сухим кератоконьюктивитом. С первых дней лечен...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/veterinarnaya-klinika-alfa_12013998/">
                            <img src="https://image2.yell.ru/imager/NDkxOTY5MjgxYjc1YzJmZTU4N/170x170/responses/6/4/3/r_1625826_19273_ayeej2dfa9wjn5oj_1690872004.webp" alt="Ветеринарная клиника Альфа" style="opacity: 1; transition: all 0.5s ease 0s;">
                                        <img class="companies__item-badge" src="/img/yell_badge/yell_badge_2024.png" alt="">
                    </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">2.</span>
                                        <meta itemprop="position" content="2">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/veterinarnaya-klinika-alfa_12013998/" itemprop="url">
                        Ветеринарная клиника Альфа                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, снт Рассвет (п Знаменский), ул Ореховая, д 225                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.8    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 96%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/veterinarnaya-klinika-alfa_12013998/reviews/"><span>18</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/veterinarnye-kliniki/">Ветеринарные клиники</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 3                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Ветеринарные аптеки                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    <a href="/krasnodar/top/salony-dlya-zhivotnykh/">Салоны для животных</a>                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                            <div class="button button_size_xxs button_theme_red company_short_button_phone_premium" ng-click="isFullPhone12013998 = true;">
                            <span class="ng-hide" ng-show="isFullPhone12013998">8 (901) 246-40-87</span>
                            <span ng-hide="isFullPhone12013998" class="company_short_button_phone_premium">8 (901) 246-40... — показать</span>
                        </div>
                                                                </div>
                </div>
                </div>
                                            <div class="companies__item-price">
                    <div class="price">
                        <div class="price__list">
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Ветеринарные услуги</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 150 руб.</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Груминг</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 700 руб. за 20 мин</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Прайс-лист</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 150 руб.</span>
                                </span>
                            </div>
                                                </div>
                    </div>
                                    </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-alfa_12013998/?reviewId=4601617">
                    <img data-lazy-src="https://www.gravatar.com/avatar/2f9298f5006b3a9b75bbd066e5d0040b?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F84%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" alt="tatyana.kolot.79" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-alfa_12013998/?reviewId=4601617">
                «Лучшая клиника! Рекомендую! Спасибо Ольге за операции. Всё прошло хорошо! Нашей Зайке удалили камень...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/veterinarnaya-klinika-kotopyos_12133744/">
                            <img data-lazy-src="https://image2.yell.ru/imager/NTUyY2IxY2QyMzVlYWQ3ZTc3Y/170x170/responses/6/5/2/r_evz4kgpdvo31oatj_1717436303.jpg" src="/img/1px.gif" alt="Ветеринарная клиника Котопёс" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">3.</span>
                                        <meta itemprop="position" content="3">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/veterinarnaya-klinika-kotopyos_12133744/" itemprop="url">
                        Ветеринарная клиника Котопёс                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул им. Евгении Жигуленко, д 11/2                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        2.7    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 54%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/veterinarnaya-klinika-kotopyos_12133744/reviews/"><span>3</span> отзыва</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/veterinarnye-kliniki/">Ветеринарные клиники</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 2                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    <a href="/krasnodar/top/salony-dlya-zhivotnykh/">Салоны для животных</a>                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                            <div class="button button_size_xxs button_theme_red company_short_button_phone_premium" ng-click="isFullPhone12133744 = true;">
                            <span class="ng-hide" ng-show="isFullPhone12133744">8 (988) 199-53-15</span>
                            <span ng-hide="isFullPhone12133744" class="company_short_button_phone_premium">8 (988) 199-53... — показать</span>
                        </div>
                                                                </div>
                </div>
                </div>
                                            <div class="companies__item-price">
                    <div class="price">
                        <div class="price__list">
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Услуги</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 300 руб.</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Вакцинация</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 100 руб.</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Терапевтические манипуляции</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 100 руб.</span>
                                </span>
                            </div>
                                                </div>
                    </div>
                                    </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-kotopyos_12133744/?reviewId=5335511">
                    <img data-lazy-src="https://image2.yell.ru/imager/NzkxMjFkZTlkNzkyZWNhOGYyO/080x080/avatar/6/2/2/a_gto00pej82a67s2f_1713545730.jpg" src="/img/1px.gif" width="40" height="40" alt="Александр Новиков" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-kotopyos_12133744/?reviewId=5335511">
                «Комментарий:
19.04.2024 г., в 16—30 по предварительной записи по телефону привезли попугая красная...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/salon-barbos_12159236/">
                            <i class="icon icon_size_m ng-scope" data-name="domashnie-zhivotnye-veterinary"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-domashnie-zhivotnye-veterinary" ng-attr-xlink:href="{{ href }}"></use></svg></i>
                                        <img class="companies__item-badge" src="/img/yell_badge/yell_badge_2024.png" alt="">
                    </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">4.</span>
                                        <meta itemprop="position" content="4">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/salon-barbos_12159236/" itemprop="url">
                        Салон Барбос                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул им. Валерия Гассия, д 21                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.5    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 90%"></span>
    </span>

    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                        <div class="companies__item-offer">
                            <a class="is-relative" href="/krasnodar/events/3517776/">
                                                             комплекс "Всё включено"                                                        </a>
                        </div>
                    </div>
                                        <div class="companies__contact">
                                            <div class="button button_size_xxs button_theme_red company_short_button_phone_premium" ng-click="isFullPhone12159236 = true;">
                            <span class="ng-hide" ng-show="isFullPhone12159236">8 (901) 246-51-07</span>
                            <span ng-hide="isFullPhone12159236" class="company_short_button_phone_premium">8 (901) 246-51... — показать</span>
                        </div>
                                                                </div>
                </div>
                </div>
                                            <div class="companies__item-price">
                    <div class="price">
                        <div class="price__list">
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Корги</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 2500 руб.</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Лабрадор</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 3000 руб.</span>
                                </span>
                            </div>
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Ливретка</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 1500 руб.</span>
                                </span>
                            </div>
                                                </div>
                    </div>
                                    </div>
                        </div>
            <div>
                            </div>
        </div>
    </div>
</div>
<div class="companies__fifth clearfix">
    <div class="companies__fifth-box">
        <span class="companies__fifth-text">Не нашли нужную компанию?</span>
        <span class="companies__fifth-gray">Вы можете добавить ее.</span>

        <a class="button button_size_s button_theme_red-linear companies__fifth-button" href="/company/create/">
            <i class="icon icon_size_m companies__fifth-icon ng-scope" data-name="add-biz"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-add-biz" ng-attr-xlink:href="{{ href }}"></use></svg></i>
            Добавить компанию        </a>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zoomagazin-u-bima_12013273/">
                            <img data-lazy-src="https://image2.yell.ru/imager/ZGY2ZGNmZDg1NDRhODg1YTNkN/170x170/responses/1/3/8/r_11800593_s1wbgh3ttxsbiimm_1455652675.jpg" src="/img/1px.gif" alt="Зоомагазин У Бима на 40-летия Победы" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-green">
                        Открыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">5.</span>
                                        <meta itemprop="position" content="5">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zoomagazin-u-bima_12013273/" itemprop="url">
                        Зоомагазин У Бима на 40-летия Победы                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул им 40-летия Победы, д 69                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.9    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 98%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/zoomagazin-u-bima_12013273/reviews/"><span>7</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/zoomagazin-u-bima_12013273/?reviewId=2391588">
                    <img data-lazy-src="https://www.gravatar.com/avatar/e521f3c4d513b292a7daf6eac44e33f8?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F65%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" alt="adekta" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/zoomagazin-u-bima_12013273/?reviewId=2391588">
                «Дешевые цены на товары и широкий выбор. Это главный плюс! Мы всегда еще пользуемся доставкой по горо...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zoovetcentr-xvostatye-gosti_12150758/">
                            <i class="icon icon_size_m ng-scope" data-name="domashnie-zhivotnye-veterinary"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-domashnie-zhivotnye-veterinary" ng-attr-xlink:href="{{ href }}"></use></svg></i>
                                        <img class="companies__item-badge" src="/img/yell_badge/yell_badge_2024.png" alt="">
                    </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">6.</span>
                                        <meta itemprop="position" content="6">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zoovetcentr-xvostatye-gosti_12150758/" itemprop="url">
                        Зооветцентр Хвостатые гости                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, проезд им. Репина, д 32                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.5    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 90%"></span>
    </span>

    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/domashnie-zhivotnye-veterinary/">Гостиницы для животных</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 2                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    <a href="/krasnodar/top/salony-dlya-zhivotnykh/">Салоны для животных</a>                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                        <div class="companies__item-offer">
                            <a class="is-relative" href="/krasnodar/events/3438574/">
                                                             Акция «Проживание более 10 дней — 10% скидка»                                                        </a>
                        </div>
                    </div>
                                        <div class="companies__contact">
                                            <div class="button button_size_xxs button_theme_red company_short_button_phone_premium" ng-click="isFullPhone12150758 = true;">
                            <span class="ng-hide" ng-show="isFullPhone12150758">8 (901) 246-39-48</span>
                            <span ng-hide="isFullPhone12150758" class="company_short_button_phone_premium">8 (901) 246-39... — показать</span>
                        </div>
                                                                </div>
                </div>
                </div>
                                            <div class="companies__item-price companies__item-price_single">
                    <div class="price">
                        <div class="price__list">
                                                    <div class="price__list-row">
                                <span class="price__list-left">
                                    <span class="price__val">Товары и услуги</span>
                                </span>
                                <span class="price__list-right">
                                    <span class="price__cost">от 200 руб.</span>
                                </span>
                            </div>
                                                </div>
                    </div>
                                    </div>
                        </div>
            <div>
                            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/grand-dog_14452762/">
                            <i class="icon icon_size_m ng-scope" data-name="domashnie-zhivotnye-veterinary"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-domashnie-zhivotnye-veterinary" ng-attr-xlink:href="{{ href }}"></use></svg></i>
                                </a>

        <div class="companies__item-content">
                        <div class="companies__item-title">
                                    <span class="companies__item-number">7.</span>
                                        <meta itemprop="position" content="7">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/grand-dog_14452762/" itemprop="url">
                        Grand Dog                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            Краснодарский край, Тихорецкий р-н, п Пригородный, ул Юбилейная, д 3                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        5.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/grand-dog_14452762/reviews/"><span>5</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/grand-dog_14452762/?reviewId=5058420">
                    <img data-lazy-src="https://www.gravatar.com/avatar/0fb3a8edca9dc7b74056ed7716752dda?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F1057%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" alt="Саня" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/grand-dog_14452762/?reviewId=5058420">
                «У меня крупная собака, для нее я заказываю микс универсал с говядиной. Он гипоаллергенный, это важно...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zveruga-net_11241080/">
                            <img data-lazy-src="https://image2.yell.ru/imager/OWY0MDUyZDE4MWRhODI0ZDY2O/170x170/responses/5/6/4/r_951157_pn7es9dm27gxxs9yx6uj.jpg" src="/img/1px.gif" alt="Zveruga.net на Тургеневском шоссе" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <div class="companies__item-title">
                                    <span class="companies__item-number">8.</span>
                                        <meta itemprop="position" content="8">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zveruga-net_11241080/" itemprop="url">
                        Zveruga.net на Тургеневском шоссе                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            Россия, Респ Адыгея, Тахтамукайский р-н, аул Новая Адыгея, ул Тургеневское шоссе, д 27                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 80%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/zveruga-net_11241080/reviews/"><span>3</span> отзыва</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review">
                            <div class="companies__item-review-avatar">
                                    <img data-lazy-src="https://www.gravatar.com/avatar/2fb8265267dd54062d2ed81bd212fa74?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F76%2Ff%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" style="opacity: 0.3;">
                            </div>
                            <div class="companies__item-review-text">«...товаров для ваших питомцев!! Огромный ассортимент. Когда заходишь в магазин-глаз радуется... Но мне кажется, на эти вещи можно только...»</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zoomagazin-barsik_12131302/">
                            <img data-lazy-src="https://image2.yell.ru/imager/ZTliMWJmODkzMjk2OTMwYmQ0M/170x170/responses/2/1/5/r_1071957_0gvat2fc08gxreemnimb.jpg" src="/img/1px.gif" alt="Зоомагазин Барсик на &ZeroWidthSpace;Восточно-Кругликовской" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">9.</span>
                                        <meta itemprop="position" content="9">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zoomagazin-barsik_12131302/" itemprop="url">
                        Зоомагазин Барсик на &ZeroWidthSpace;Восточно-Кругликовской                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул Восточно-Кругликовская, д 46/11                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        3.4    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 68%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/zoomagazin-barsik_12131302/reviews/"><span>27</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/zoomagazin-barsik_12131302/?reviewId=2098383">
                    <img data-lazy-src="https://pp.vk.me/c625328/v625328296/4e14f/qGdVkFW3BX0.jpg" src="/img/1px.gif" width="40" height="40" alt="Юлик Горбач" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/zoomagazin-barsik_12131302/?reviewId=2098383">
                «Отличный зоомагазин. В этом месте я приобрел для своей собачки несколько вещей, порода у моего питом...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zveruga-net_11241078/">
                            <i class="icon icon_size_m ng-scope" data-name="domashnie-zhivotnye-veterinary"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-domashnie-zhivotnye-veterinary" ng-attr-xlink:href="{{ href }}"></use></svg></i>
                                </a>

        <div class="companies__item-content">
                        <div class="companies__item-title">
                                    <span class="companies__item-number">10.</span>
                                        <meta itemprop="position" content="10">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zveruga-net_11241078/" itemprop="url">
                        Zveruga.net на Крылатой улице                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            Россия, г Краснодар, ул Крылатая, д 2                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        5.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

            <span class="rating__reviews">
                          <span>2</span> отзыва                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review">
                            <div class="companies__item-review-avatar">
                                    <img data-lazy-src="https://www.gravatar.com/avatar/c07ef970b591608802dad60f4c59a9d5?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F69%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" style="opacity: 0.3;">
                            </div>
                            <div class="companies__item-review-text">«...нашла его только в Зверюге. Отдала всего лишь 50 рублей. При этом консультант дала очень важные и дельные советы по уходу за моим...»</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__reviews clearfix">
    <h4 class="companies__reviews-title">Свежие отзывы в категории «Зоомагазины»</h4>

                    <div class="reviews__item">
                            <div class="reviews__item-user">
                    <div class="reviews__item-user-avatar">
                        <img data-lazy-src="https://image2.yell.ru/avatar/no_avatar/1051/m/80/avatar.png" src="/img/1px.gif" width="60" height="60" alt="" style="opacity: 0.3;">
                    </div>
                    <div class="reviews__item-user-name">Лен</div>
                </div>
            
            <div class="reviews__item-content">
                <div class="is-color-red">
                    <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-bolshaya-medveditsa_10193908/">
                        Ветеринарная клиника Большая Медведица                    </a>
                </div>
                
<div class="rating rating_size_m">    <span class="rating__value">
        5    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

    </div>                <span class="reviews__item-added">
                     26 декабря 2023 12:13                </span>

                <div class="reviews__item-text">Наблюдаемся у Карины Гаджиевны уже больше 2х месяцев с сердцем у котика. Очень х...</div>
                <a class="link link_underline" href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-bolshaya-medveditsa_10193908/?reviewId=5192645">
                    читать дальше                </a>
            </div>
        </div>
    </div>
<!--AdFox START-->
<!--yandex_yellkloss-admanager-->
<!--Площадка: yell.ru / Desktop / Catalog Desktop-->
<!--Категория: <не задана>-->
<!--Тип баннера: Billboard-->
<div id="adfox_169825660941521732_110"></div>
<script>
    window.yaContextCb.push(() => {
        Ya.adfoxCode.createAdaptive({
            ownerId: 1511119,
            containerId: 'adfox_169825660941521732_110',
            params: {
                p1: 'czvvh',
                p2: 'iqle'
            },
            lazyLoad: {
                fetchMargin: 100,
                mobileScaling: 1,
            },
        }, ['desktop', 'tablet'], {
            tabletWidth: 830,
            phoneWidth: 480,
            isAutoReloads: false
        });
    });
</script>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/internet-magazin-bonnifacii-ru_12013295/">
                            <img data-lazy-src="https://image2.yell.ru/imager/NjhlYWZhZGEwNzZlMmY1ZjYzY/170x170/responses/9/9/1/r_1510821_qac3vsafve88a1hr_1497980037.jpg" src="/img/1px.gif" alt="Интернет-магазин Bonnifacii.ru" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">11.</span>
                                        <meta itemprop="position" content="11">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/internet-magazin-bonnifacii-ru_12013295/" itemprop="url">
                        Интернет-магазин Bonnifacii.ru                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул Душистая, д 41                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        5.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

            <span class="rating__reviews">
                          <span>2</span> отзыва                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/internet-magazin-bonnifacii-ru_12013295/?reviewId=3249379">
                    <img data-lazy-src="https://www.gravatar.com/avatar/a0e561b237ab9fc4d6c7deb6ef31122a?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F75%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" alt="kir-ver2014" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/internet-magazin-bonnifacii-ru_12013295/?reviewId=3249379">
                «Заказывали корм собаке, привезли в этот же день. Менеджеры тактичные, цены нормальные. По листовке н...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/barsik_10192759/">
                            <i class="icon icon_size_m ng-scope" data-name="domashnie-zhivotnye-veterinary"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-domashnie-zhivotnye-veterinary" ng-attr-xlink:href="{{ href }}"></use></svg></i>
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">12.</span>
                                        <meta itemprop="position" content="12">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/barsik_10192759/" itemprop="url">
                        Зоомагазин Барсик в Краснодаре                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, пр-кт Чекистов, д 13                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        5.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

            <span class="rating__reviews">
                          <span>1</span> отзыв                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/barsik_10192759/?reviewId=2348112">
                    <img data-lazy-src="https://image2.yell.ru/imager/MjllNDc0ZDA1NGRlMzhlMTAxM/080x080/avatar/5/2/9/a_1101953_1y01jnq00lg6rnbpp5pi.jpg" src="/img/1px.gif" width="40" height="40" alt="poranish_posolyu" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/barsik_10192759/?reviewId=2348112">
                «В Барсике всегда низкие цены и большой выбор товаров. От необходимого (вет.препараты, ошейники от па...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zoo-yug_10204578/">
                            <i class="icon icon_size_m ng-scope" data-name="domashnie-zhivotnye-veterinary"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-domashnie-zhivotnye-veterinary" ng-attr-xlink:href="{{ href }}"></use></svg></i>
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-green">
                        Открыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">13.</span>
                                        <meta itemprop="position" content="13">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zoo-yug_10204578/" itemprop="url">
                        Ветеринарный центр Зоо-Юг на проспекте Чекистов                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, пр-кт Чекистов, д 31/2                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 80%"></span>
    </span>

            <span class="rating__reviews">
                          <span>2</span> отзыва                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 3                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Ветеринарные аптеки                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    <a href="/krasnodar/top/salony-dlya-zhivotnykh/">Салоны для животных</a>                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    <a href="/krasnodar/top/akvariumy-i-akvariumistika/">Аквариумы и аквариумистика</a>                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review">
                            <div class="companies__item-review-avatar">
                                    <img data-lazy-src="https://pp.vk.me/c625418/v625418257/44754/Amu8OZWBpjQ.jpg" src="/img/1px.gif" width="40" height="40" style="opacity: 0.3;">
                            </div>
                            <div class="companies__item-review-text">«...находим в сети магазинов Зоо Юг все самое необходимое для домашних питомцев.Здесь самые низкие цены в городе, большой выбор товаров...»</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/magazin-zootovarov-ip-sokolov-a-n_11240606/">
                            <i class="icon icon_size_m ng-scope" data-name="domashnie-zhivotnye-veterinary"><svg width="16" height="16"><use xlink:href="/assets/1c1cb910/svg/sprite.common.svg#symbol-domashnie-zhivotnye-veterinary" ng-attr-xlink:href="{{ href }}"></use></svg></i>
                                </a>

        <div class="companies__item-content">
                        <div class="companies__item-title">
                                    <span class="companies__item-number">14.</span>
                                        <meta itemprop="position" content="14">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/magazin-zootovarov-ip-sokolov-a-n_11240606/" itemprop="url">
                        Магазин зоотоваров, ИП Соколов А.Н.                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            Россия, г Краснодар, ул 1-я Линия Нефтяников, д 148                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        5.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

            <span class="rating__reviews">
                          <span>1</span> отзыв                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 1                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    <a href="/krasnodar/top/akvariumy-i-akvariumistika/">Аквариумы и аквариумистика</a>                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/magazin-zootovarov-ip-sokolov-a-n_11240606/?reviewId=2143801">
                    <img data-lazy-src="https://www.gravatar.com/avatar/f3f702e6dca31f2c06889d79648397e0?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F65%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" alt="angelina.shimanskaya.1990" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/magazin-zootovarov-ip-sokolov-a-n_11240606/?reviewId=2143801">
                «В этом зоомагазине я покупала все для своей черепахи, тогда она еще была маленькая, но сейчас вымаха...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/le-murrr_11247334/">
                            <img data-lazy-src="https://irs0.4sqi.net/img/general/original/82085457_kJJAgJTn5YZrmRAbvNqz5nm7IxRJAQekSm8essX6AZM.jpg" src="/img/1px.gif" alt="Ле'муррр в Западном округе" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <div class="companies__item-title">
                                    <span class="companies__item-number">15.</span>
                                        <meta itemprop="position" content="15">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/le-murrr_11247334/" itemprop="url">
                        Ле'муррр в Западном округе                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            Россия, г Краснодар, проезд им Тургенева, д 124                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        5.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

            <span class="rating__reviews">
                          <span>1</span> отзыв                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review">
                            <div class="companies__item-review-avatar">
                                    <img data-lazy-src="https://www.gravatar.com/avatar/aa8d5c1737ba0986d1c8e213d4e7dc9e?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F68%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" style="opacity: 0.3;">
                            </div>
                            <div class="companies__item-review-text">«...магазин,небольшой но очень уютный.Качественное обслуживание,очень отзывчивые продавцы,ни когда не грубят,всегда готовы помочь в...»</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zoovettsentr_11891834/">
                            <img data-lazy-src="https://image2.yell.ru/imager/NzgwMjdlY2ZhMTE1OTRkZTBkY/170x170/responses/1/0/1/r_zoovettsentr-11891834-zttz2byf1r_1551727871.jpg" src="/img/1px.gif" alt="Зооцентр на Целиноградской улице" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-green">
                        Открыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">16.</span>
                                        <meta itemprop="position" content="16">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zoovettsentr_11891834/" itemprop="url">
                        Зооцентр на Целиноградской улице                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, поселок Березовый, ул Целиноградская, д 68                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        4.7    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 94%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/zoovettsentr_11891834/reviews/"><span>26</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/veterinarnye-kliniki/">Ветеринарные клиники</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 3                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Ветеринарные аптеки                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Гостиницы для животных                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review">
                            <div class="companies__item-review-avatar">
                                    <img data-lazy-src="https://image2.yell.ru/imager/YTdjYzJmNTBmN2E5M2E4MDE0Z/080x080/avatar/6/6/0/a_hy387wra96oz3r6r_1540485407.jpg" src="/img/1px.gif" width="40" height="40" style="opacity: 0.3;">
                            </div>
                            <div class="companies__item-review-text">«...советую, если у вас заболел ваш питомец!!!! Грамотный и внимательный персонал (положительные и открытые люди) Привезла мою девочку...»</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/veterinarnaya-klinika-bagira-na-ulice-ehngelsa_11940847/">
                            <img data-lazy-src="https://image2.yell.ru/imager/Yjk3YWZjNjJkYWMwNzNhZDhmN/170x170/responses/8/1/5/r_5yerte2fuetxqapx_1615883851.jpg" src="/img/1px.gif" alt="Ветеринарная клиника Багира на улице Энгельса" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-green">
                        Открыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">17.</span>
                                        <meta itemprop="position" content="17">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/veterinarnaya-klinika-bagira-na-ulice-ehngelsa_11940847/" itemprop="url">
                        Ветеринарная клиника Багира на улице Энгельса                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            Краснодарский край, г Новороссийск, ул Энгельса, д 70                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        5.0    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 100%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/veterinarnaya-klinika-bagira-na-ulice-ehngelsa_11940847/reviews/"><span>5</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/veterinarnye-kliniki/">Ветеринарные клиники</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 3                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Ветеринарные аптеки                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Гостиницы для животных                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-bagira-na-ulice-ehngelsa_11940847/?reviewId=4312670">
                    <img data-lazy-src="https://image2.yell.ru/imager/Yzk4NWY5MGRjNDE5N2E1NWVkN/080x080/avatar/2/7/7/a_d54vp8zb8ehtyvmr_1651222354.jpg" src="/img/1px.gif" width="40" height="40" alt="Алина" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-bagira-na-ulice-ehngelsa_11940847/?reviewId=4312670">
                «Отличная клиника. Хорошое отношение к животным. Очень хорошие врачи.»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/zoomagazin-barsik_12131761/">
                            <img data-lazy-src="https://image2.yell.ru/imager/MTBhOWMwOWE2OTMwMmRhNjg4N/170x170/responses/5/6/6/r_zoomagazin-barsik-12131761-tjx82y5w5w_1676886435.jpg" src="/img/1px.gif" alt="Зоомагазин Барсик на Уральской" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">18.</span>
                                        <meta itemprop="position" content="18">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/zoomagazin-barsik_12131761/" itemprop="url">
                        Зоомагазин Барсик на Уральской                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул Уральская, д 95 к 1                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        3.7    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 74%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/zoomagazin-barsik_12131761/reviews/"><span>3</span> отзыва</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                Зоомагазины                            </span>
                                                                    </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/zoomagazin-barsik_12131761/?reviewId=2105144">
                    <img data-lazy-src="https://www.gravatar.com/avatar/f3f702e6dca31f2c06889d79648397e0?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F65%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" alt="angelina.shimanskaya.1990" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/zoomagazin-barsik_12131761/?reviewId=2105144">
                «Чудесный зоомагазин "Барсик", открыла его для себя не так давно. Искала новые игрушки для своего кот...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/lapaclinic_11872444/">
                            <img data-lazy-src="https://image2.yell.ru/imager/MWI0YWViYjVjOTRjYmM5ODM1O/170x170/responses/6/4/7/r_1403348_spyfybhd7j2z4bbl_1480333062.jpg" src="/img/1px.gif" alt="Лапа Помощи в Прикубанском округе" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-green">
                        Открыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">19.</span>
                                        <meta itemprop="position" content="19">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/lapaclinic_11872444/" itemprop="url">
                        Лапа Помощи в Прикубанском округе                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул им Архитектора Ишунина, д 7/1 к 2                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        3.9    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 78%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/lapaclinic_11872444/reviews/"><span>11</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/veterinarnye-kliniki/">Ветеринарные клиники</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 3                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Ветеринарные аптеки                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Гостиницы для животных                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review">
                            <div class="companies__item-review-avatar">
                                    <img data-lazy-src="https://www.gravatar.com/avatar/72e601654c456a49af744aa9852d2d2c?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F78%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" style="opacity: 0.3;">
                            </div>
                            <div class="companies__item-review-text">«...В этой клинике можно максимум сделать прививку. Если питомец реально заболел-обходите стороной. Моя история вкратце-у собаки была...»</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="companies__item clearfix" itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
    <div class="companies__item-container">
        <a class="companies__item-image" href="/krasnodar/com/veterinarnaya-klinika-ajbolit-na-rashpilevskoj-ulice_12013947/">
                            <img data-lazy-src="https://image2.yell.ru/imager/OTVmNDdkNzBjOGQ4OTJkM2Y1M/170x170/responses/0/5/7/r_1253236_jfzphj973unsp0z5_1453547699.jpg" src="/img/1px.gif" alt="Ветеринарная клиника Айболит на Рашпилевской улице" style="opacity: 0.3;">
                                </a>

        <div class="companies__item-content">
                        <span class="companies__item-working">
                                    <span class="companies__item-working-status is-color-red">
                        Закрыто сейчас                    </span>
                            </span>
                        <div class="companies__item-title">
                                    <span class="companies__item-number">20.</span>
                                        <meta itemprop="position" content="20">
                                    
                <h2>
                    <a class="companies__item-title-text" href="/krasnodar/com/veterinarnaya-klinika-ajbolit-na-rashpilevskoj-ulice_12013947/" itemprop="url">
                        Ветеринарная клиника Айболит на Рашпилевской улице                    </a>
                </h2>

                            </div>

            
            <div class="companies__grid">
                                <div class="companies__item-info">
                    <div class="companies__grid-block companies__grid-block_right">

                        <div class="companies__item-address">
                            г Краснодар, ул Рашпилевская, д 26                        </div>

                                            </div>
                    <div class="companies__grid-block companies__grid-block_left">
                                            <div class="companies__item-rating">
                            
<div class="rating rating_size_m">    <span class="rating__value">
        3.7    </span>

    <span class="rating__stars">
        <span class="rating__stars-empty"></span>
    <span class="rating__stars-fill" style="width: 74%"></span>
    </span>

            <span class="rating__reviews">
                          <a href="/krasnodar/com/veterinarnaya-klinika-ajbolit-na-rashpilevskoj-ulice_12013947/reviews/"><span>16</span> отзывов</a>                    </span>
    </div>                        </div>
                    
                    <div class="companies__item-category">
                                                    <span>
                                <a href="/krasnodar/top/veterinarnye-kliniki/">Ветеринарные клиники</a>,                            </span>
                                                                            <div class="companies__item-more">
                                <span class="link link_pseudo">
                                    еще 2                                </span>
                                <div class="popup popup_pos_right-center ng-scope">
                                    <div class="popup__content">
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Зоомагазины                                                                                            </div>
                                                                                    <div class="is-white-space-nowrap">
                                                                                                    Ветеринарные аптеки                                                                                            </div>
                                                                            </div>
                                    <span class="popup__triangle"></span>
                                </div>
                            </div>
                                            </div>
                                        <div class="companies__contact">
                                                                </div>
                </div>
                </div>
                        </div>
            <div>
                    <div class="companies__item-review            companies__item-review_avatar">
                    <div class="companies__item-review-avatar">
                <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-ajbolit-na-rashpilevskoj-ulice_12013947/?reviewId=2318530">
                    <img data-lazy-src="https://www.gravatar.com/avatar/e7bc41f60e7917d88b619b064e64e072?s=80&amp;d=https%3A%2F%2Fimage2.yell.ru%2Favatar%2Fno_avatar%2F90%2Fm%2F80%2Favatar.png" src="/img/1px.gif" width="40" height="40" alt="zaira1984" style="opacity: 0.3;">
                </a>
            </div>
                <div class="companies__item-review-text">
            <a href="//www.yell.ru/krasnodar/com/veterinarnaya-klinika-ajbolit-na-rashpilevskoj-ulice_12013947/?reviewId=2318530">
                «18.06.2015 Джесику убили мою. В первый день не смогли сделать капельницу "врачи". На второй день ей...»
            </a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<!--AdFox START-->
<!--yandex_yellkloss-admanager-->
<!--Площадка: yell.ru / Desktop / Catalog Desktop-->
<!--Категория: <не задана>-->
<!--Тип баннера: Billboard-->
<div id="adfox_169825660941521732_120"></div>
<script>
    window.yaContextCb.push(() => {
        Ya.adfoxCode.createAdaptive({
            ownerId: 1511119,
            containerId: 'adfox_169825660941521732_120',
            params: {
                p1: 'czvvh',
                p2: 'iqle'
            },
            lazyLoad: {
                fetchMargin: 100,
                mobileScaling: 1,
            },
        }, ['desktop', 'tablet'], {
            tabletWidth: 830,
            phoneWidth: 480,
            isAutoReloads: false
        });
    });
</script>
    </div>
    """,
    # Добавьте сюда другие HTML фрагменты
]

output_path = 'companies.xlsx'  # путь к выходному файлу Excel
process_html_fragments(html_fragments, output_path)