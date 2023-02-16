import requests
from bs4 import BeautifulSoup as bs
import json

get_html = requests.get('https://books.toscrape.com/')
html = get_html.content
soup = bs(html, 'html.parser')
sections = soup.select('section')
section = sections[0]

books_block = section.select_one('ol[class=row]')
books = books_block.select('li')

books_data = []
for book in books:
    image = 'https://books.toscrape.com/'+ book.find('div', attrs={'class': 'image_container'}).find('img')['src']
    title = book.find('h3').find('a')['title']
    price = book.find('p', attrs={'class': 'price_color'}).text

    book_dict = {
        'image' : image,
        'title' : title,
        'price' : price,
    }
    books_data.append(book_dict)
    with open('data.json', 'a+') as file:
        json.dump(book_dict, file, indent=8)
print(books_data)

