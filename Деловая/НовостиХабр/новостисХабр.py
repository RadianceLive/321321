import requests
from bs4 import BeautifulSoup
import sqlite3
import argparse
import datetime

DB_NAME = "news.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        link TEXT,
        date_scraped TEXT
    )''')
    conn.commit()
    conn.close()

def scrape_habr():
    print("Парсим новости с habr.com...")
    url = "https://habr.com/ru/all/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    articles = soup.find_all("article")
    data = []

    for a in articles[:5]:
        title_tag = a.find("h2")
        if title_tag:
            title = title_tag.text.strip()
            link = "https://habr.com" + title_tag.find("a")["href"]
            data.append((title, link, datetime.datetime.now().isoformat()))

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.executemany("INSERT INTO news (title, link, date_scraped) VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()
    print(f"✅ Добавлено {len(data)} новостей.")

def list_news():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for row in c.execute("SELECT id, title, link FROM news ORDER BY id DESC LIMIT 10"):
        print(f"{row[0]}. {row[1]}\n   {row[2]}\n")
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="News Parser")
    parser.add_argument('--scrape', action='store_true', help='Парсить новости')
    parser.add_argument('--list', action='store_true', help='Показать последние новости')
    args = parser.parse_args()

    init_db()
    if args.scrape:
        scrape_habr()
    elif args.list:
        list_news()
    else:
        parser.print_help()