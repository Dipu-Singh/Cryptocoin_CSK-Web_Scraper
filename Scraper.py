
import pandas as pd
import requests
import operator
from bs4 import BeautifulSoup
import smtplib
import time
import os
from playsound import playsound
#--------------Variable---------------#
# enter your value here
# or use this https://coinswitch.co/coins/bitcoin/bitcoin-to-inr
url = "https://coinswitch.co/coins/ripple/ripple-to-inr"
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}


def price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    # find by class use attrs{"ClassName"}
    title = soup.find(id="assetContainer").get_text()
    Sp = title.split()
    # print(title)  # $34,712.47
    # print(type(title))
    # print('----String Selection----')
    # print(Sp)
    print(len(Sp))
    L = list(Sp)  # String - List
    # print(type(L))
    # print(L)

    # Removal of INR & ₹
    for i in L:
        if i == '/INR':
            L.remove(i)
        else:
            pass

    for i in L:
        if i == '₹':
            L.remove(i)
    # print(L)

    def Convert(lst):
        res_dct = {lst[i]: float(lst[i + 1]) for i in range(0, len(lst), 2)}
        return res_dct

    # print(Convert(L))  # dict converted data
    sorted_dict = dict(sorted(Convert(L).items(), key=operator.itemgetter(0)))

    # print(type(sorted_dict))
    print(sorted_dict)

    # we can use header=1/0/None
    data = pd.read_csv('Test.csv')
    # data2 = pd.DataFrame(d
    data_user = dict(zip(dict(data.Coin_Name).values(),
                     dict(data.Value).values()))
    print(data_user)

    print(type(data_user))
    # print(data_user.keys())
    passlist = []
    passlist.clear()  # to empty it for next cycle
    for i in data_user.keys():
        if i in sorted_dict.keys():
            # print('Present: ', i)
            if data_user.get(i) < sorted_dict.get(i):
                print('Buy Green: ', i)
                passlist.append(i)
            elif data_user.get(i) == sorted_dict.get(i):
                print('Buy Yellow: ', i)
                passlist.append(i)
            else:
                print('Buy Red: ', i)
        else:
            print('not match: ', i)
    email(passlist)

#-----------------------------Send Mail------------------------------#


def email(passlist):
    if len(passlist) != 0:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('sender_email@gmail.com', 'aadnukfpkwqhhlqh')
        subject = 'Set Coin Price Fell Down! : ' + \
            ', '.join(passlist)  # list -> str
        body = 'Need to open on android app: https://coinswitch.sng.link/A6to7/48zh?_ios_dl=https://kuber.page.link/home&amp;_android_dl=coinswitch://'
        msg = f"Subject : {subject}\n\n{body}"
        server.sendmail('sender_email@gmail.com', 'recipient_email@gmail.com', msg)
        print('Email has been sent')
        playsound('SMS Tone.mp3')
        server.quit()
    else:
        print('No COIN fulfill Condn!')


# Timer ----- To Run continuously
n = 0
# for x in range(1800):
while(True):
    price()
    print('Cycle turn:', n)
    time.sleep(15)  # to wait in second
    os.system('cls')  # to clear previous number
    # use ('clear') if you are using linux/mac
    n = n+1
