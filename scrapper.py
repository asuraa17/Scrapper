# git config --global user.name "Name"
# git config --global user.email "email.com"

# git init 
# git status => if you want to check the status of the files 
# git diff => if you want to check the changes
# git add .
# git commit -m "your message"
# copy paste git code from github

# 1. change the code
# 2. git add .
# 3. git commit -m "your message"
# 4. git push

#refactor

import requests
import json
import csv

from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Fialed to open page")
        return[]
    
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_ = "product_pod")

    book_list = []
    for book in books:
        title = book.h3.a['title']
        price_text = book.find('p', class_ = 'price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        book_list.append(
            {
                "title": title,
                "currency": currency,
                "price": price
            }
        )

        return book_list
    
all_books = scrape_books(url)

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(all_books, f, indent=4, ensure_ascii=False)

with open("books.csv", "w", newline="", encoding="utf-g") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "currency","price"])
    writer.writeheader()
    writer.writerrows(all_books)