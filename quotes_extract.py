import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://www.keepinspiring.me/quotes-about-smiling/')
soup = BeautifulSoup(page.content, 'html.parser')
names = []
quote = []
for quotes in soup.find_all(class_='author-quotes'):
    quote.append((quotes.get_text()))
    names.append(quotes.find(class_='quote-author-name').get_text())

quotes_all=pd.DataFrame({
    'quotes':quote,
    'author':names
})
#print(quotes_all)
quotes_all.to_csv('smile_quotes.csv')
