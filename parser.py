# 1.Парсер однопоточный
# 2.Замер времени
# 3.multiprocessing Pool
# 4.замер времени
# 5.экспорт в csv
# pip install requests
# pip install beautifulsoup4
# Надо установить парсер pip install lxml

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)                                                   # Response
    return r.text                                                           # возвращает HTML-код страницы (url)

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    tds = soup.find('table', id='currencies').find_all('td', class_='currency-name')        # список об. soup-а
# class зарезервированное в python слово, используем class_
    links = []

    for td in tds:
        a = td.find('a', class_='link-secondary').get('href')                               # string
        link = 'https://coinmarketcap.com' + a                                              # в виде полной ссылки
        links.append(link)

    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        name = soup.find('h1', class_='details-panel-item--name').find('span', class_='h3').text.strip()
    except:
        name = ''

    try:
        price = soup.find('span', id='quote_price').find('span', class_='h2').text.strip()
    except:
        price = ''

    data = {'name': name, 
            'price': price }
    return data

def write_scv(data):
    with open('coinmarketcap.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow( (data['name'], 
                          data['price']) )
        print(data['name'] + ' parsed')


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_scv(data)



def main():
    start = datetime.now()

    url =  'https://coinmarketcap.com/'
    
    all_links = get_all_links( get_html(url) )
    
    # for url in all_links:
    #     html = get_html(url)
    #     data = get_page_data(html)
    #     write_scv(data)

    with Pool(5) as p:
        p.map(make_all, all_links)                   # передаем функцию а не результат поэтому make_all без ()




    end = datetime.now()
    total = end - start
    print(str(total))

if __name__ == '__main__':
    main()


