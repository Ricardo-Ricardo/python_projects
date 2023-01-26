### This script will check the price of a item on amazon and if its lower than the selected price then it will send an email ###
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import time

### URL for item --- Lego Millennium Falcon ---
URL = "https://www.amazon.com/LEGO-Ultimate-Millennium-Falcon-Building/dp/B075SDMMMV/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.14a246c3-7a62-40bf-bdd0-5ac67c2a1913%3Aamzn1.sym.14a246c3-7a62-40bf-bdd0-5ac67c2a1913&cv_ct_cx=lego+millennium+falcon&keywords=lego+millennium+falcon&pd_rd_i=B075SDMMMV&pd_rd_r=926479ca-fa1b-407d-8d13-f05e54eaa4c2&pd_rd_w=1491J&pd_rd_wg=03xMj&pf_rd_p=14a246c3-7a62-40bf-bdd0-5ac67c2a1913&pf_rd_r=PAF8HB17HT4MKEH87F7D&qid=1673650298&sprefix=lego+mileniu%2Caps%2C192&sr=1-1-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&ufe=app_do%3Aamzn1.fos.2b70bf2b-6730-4ccf-ab97-eb60747b8daf&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUEZDQlo5RkJHSzFOJmVuY3J5cHRlZElkPUEwMjY0NjUyM1M2U0tRR0laVFRSMCZlbmNyeXB0ZWRBZElkPUEwMjI4MjE1N1RMMExZTVVKNTNFJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
    'Accept-Language': 'en-US, en;q=0.5'})

### Web scraping using BeautifulSoup
def check_price():
    page = requests.get(URL, headers=HEADERS) # http request
    soup = BeautifulSoup(page.content, "lxml")
    
    global title; title = "" # title and price are used in send_mail()
    global price; price = "" 
    try:
        title = soup.find("span", attrs={"id": 'productTitle'}).string.strip().replace(',', '') # removes the comma
        title = title[:47] # shorten the title to desired length
    except AttributeError: # if nothing is found, return NA
        title = "NA"
    
    try:
        price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '') # removes the comma
    except AttributeError: # if nothing is found, return NA
        price = "NA"

    converted_price = float(price[1:]) # remove the dollar sign to be converted into a float for price comparison

    print("product Title = ", title)
    print("product Price = ", converted_price)
    if(converted_price < 700): # set the minimum price amount in order to send mail
        send_mail()

### send email of item with the link attached as a hyperlink with html
def send_mail():
    email = 'kylerobert@gmail.com' # sender
    send_to = 'ricky.misc99@gmail.com' # reciever
    subject = title + " Price Fell Down!"
    messageHTML = (title + " has dropped to " + price + '<p> Check it out on amazon <a href="https://www.amazon.com/LEGO-Ultimate-Millennium-Falcon-Building/dp/B075SDMMMV/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.14a246c3-7a62-40bf-bdd0-5ac67c2a1913%3Aamzn1.sym.14a246c3-7a62-40bf-bdd0-5ac67c2a1913&cv_ct_cx=lego+millennium+falcon&keywords=lego+millennium+falcon&pd_rd_i=B075SDMMMV&pd_rd_r=926479ca-fa1b-407d-8d13-f05e54eaa4c2&pd_rd_w=1491J&pd_rd_wg=03xMj&pf_rd_p=14a246c3-7a62-40bf-bdd0-5ac67c2a1913&pf_rd_r=PAF8HB17HT4MKEH87F7D&qid=1673650298&sprefix=lego+mileniu%2Caps%2C192&sr=1-1-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&ufe=app_do%3Aamzn1.fos.2b70bf2b-6730-4ccf-ab97-eb60747b8daf&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUEZDQlo5RkJHSzFOJmVuY3J5cHRlZElkPUEwMjY0NjUyM1M2U0tRR0laVFRSMCZlbmNyeXB0ZWRBZElkPUEwMjI4MjE1N1RMMExZTVVKNTNFJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==">here</a>')
    messagePlain = title + " price has dropped to " + price

    msg = MIMEMultipart('alternative')
    msg['From'] = email
    msg['To'] = send_to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(messagePlain, 'plain')) # adds both the plain and html parts to the email
    msg.attach(MIMEText(messageHTML, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587) # default port smtp uses
    server.ehlo() # used to identify itself when connecting to another email server
    server.starttls() # tells an email server that the email client wants a secure connection
    server.ehlo() # establishes connection again
    server.login('kylerobert@gmail.com', 'svxurllkxskihzda') # generated app password
    server.sendmail('kylerobert@gmail.com', 'ricky.misc99@gmail.com', msg.as_string())
    
    print('Email has been sent')
    server.quit() # close connections

while(True): # never stops checking price
    check_price()
    time.sleep(86400) # checks once a day, 60 * 60 * 24