import requests
from bs4 import BeautifulSoup
import smtplib
import time

email_adress = "dangremontjayson.pro@gmail.com"

n = int(input("Number of url you want track (2 max) : "))
url = {}

for i in range(n):
    text = input("Your url(s) : ").split()
    url[text[0]] = text[1]

prices = list((url.values()))
urls = list((url.keys()))

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def check_price():

    product_price = []

    if n == 1:
        page_1 = requests.get(urls[0], headers=headers)
        bsoup_1 = BeautifulSoup(page_1.content, "html5lib")
        product_price.append(bsoup_1.find(id='priceblock_ourprice').get_text().strip()[0:3])

        if product_price[0] >= prices[0]:
            send_email()
        else:
            print("Not yet")
            pass

    elif n == 2:
        page_1 = requests.get(urls[0], headers=headers)
        bsoup_1 = BeautifulSoup(page_1.content, "html5lib")

        page_2 = requests.get(urls[1], headers=headers)
        bsoup_2 = BeautifulSoup(page_2.content, "html5lib")

        product_price.append(bsoup_1.find(id='priceblock_ourprice').get_text().strip()[0:3])
        product_price.append(bsoup_2.find(id='priceblock_ourprice').get_text().strip()[0:3])

        if product_price[0] >= prices[0]:
            send_email()
        else:
            print("Not yet")
            pass
        if product_price[1] >= prices[1]:
            send_email()
        else:
            print("Not yet")
            pass

    else:
        print("Put a valid number")

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email_adress, 'Your app password')

    subject = "You can buy it !"

    if n == 1:
        body = 'You can buy it !', "1: ", urls[0]
    elif n == 2:
        body = 'You can buy it !', "1: ", urls[0], "2: ", urls[1]
    else:
        body = None

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        email_adress,
        email_adress,
        msg
    )

    print("L'Email a été envoyé !")

    server.quit()

while(True):
    check_price()
    time.sleep(86400)