import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/LEGO-Ultimate-Millennium-Falcon-Building/dp/B075SDMMMV/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.14a246c3-7a62-40bf-bdd0-5ac67c2a1913%3Aamzn1.sym.14a246c3-7a62-40bf-bdd0-5ac67c2a1913&cv_ct_cx=lego+millennium+falcon&keywords=lego+millennium+falcon&pd_rd_i=B075SDMMMV&pd_rd_r=926479ca-fa1b-407d-8d13-f05e54eaa4c2&pd_rd_w=1491J&pd_rd_wg=03xMj&pf_rd_p=14a246c3-7a62-40bf-bdd0-5ac67c2a1913&pf_rd_r=PAF8HB17HT4MKEH87F7D&qid=1673650298&sprefix=lego+mileniu%2Caps%2C192&sr=1-1-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&ufe=app_do%3Aamzn1.fos.2b70bf2b-6730-4ccf-ab97-eb60747b8daf&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUEZDQlo5RkJHSzFOJmVuY3J5cHRlZElkPUEwMjY0NjUyM1M2U0tRR0laVFRSMCZlbmNyeXB0ZWRBZElkPUEwMjI4MjE1N1RMMExZTVVKNTNFJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
    'Accept-Language': 'en-US, en;q=0.5'})
 
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
 
product_name = ''
product_price = ''
try:
    product_title = soup.find("span",
                              attrs={"id": 'productTitle'})
    product_name = product_title.string.strip().replace(',', '')
 
except AttributeError:
    product_name = "NA"
 
try:
    product_price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
except AttributeError:
    product_price = "NA"
 
print("product Title = ", product_name)
print("product Price = ", product_price)