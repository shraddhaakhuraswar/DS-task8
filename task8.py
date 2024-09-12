import requests as rq
import pandas as pd
from bs4 import BeautifulSoup

qurl='https://books.toscrape.com/'
qheader={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
qresp=rq.get(url=qurl,headers=qheader)
bsoup=BeautifulSoup(qresp.content,"html.parser")

qdata=bsoup.findAll('article',class_='product_pod')

alldata=[]
for item in qdata:
    title = item.h3.a['title']
    price = item.find('p',class_='price_color').text
    rating = item.p['class'][1]

    booksdata={
        'title':title,
        'price':price,
        'rating':rating
    }
    alldata.append(booksdata)

print(alldata)
qpd=pd.DataFrame(alldata)
qpd.to_csv('books.csv')