import requests
from bs4 import BeautifulSoup

#URL = 'https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/dp/B07P6Y7954/ref=sr_1_11?crid=1JSDZFICIB1I1&keywords=iphone&qid=1673651756&sprefix=iphone%2Caps%2C2730&sr=8-11'
URL = 'https://www.target.com/p/lego-star-wars-501st-clone-troopers-battle-pack-75345-building-toy-set/-/A-86216264#lnk=sametab'
#URL = 'https://www.lego.com/en-us/product/501st-clone-troopers-battle-pack-75345'
#headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")
title = soup.find(id="mw-content-text").get_text()
title = soup.find("span", {"class": "product-price", "data-test": True})['data-test']
print(title.strip())
with requests.Session() as s:
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'
    res = s.get(URL)
    soup = BeautifulSoup(res.text,"html.parser")
    price = soup.select_one("td[data-test='product-price'] > div")
    print(price)
