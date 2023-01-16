import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/dp/B07P6Y7954/ref=sr_1_11?crid=1JSDZFICIB1I1&keywords=iphone&qid=1673651756&sprefix=iphone%2Caps%2C2730&sr=8-11'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")
print(title)
