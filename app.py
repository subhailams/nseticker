from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import bs4 as bs
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER = os.environ['CHROME_DRIVER']

options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=options)
driver.get("https://nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=MRF&illiquid=0&smeFlag=0&itpFlag=0")
content = driver.find_elements_by_class_name("stock")

price = ""
List = []

for i in content:
    price += i.text

List = list(map(str,price.split("\n")))

priceList = {}
priceList['Last Price'] = List[0]
priceList['Open Price'] = List[5]
priceList['High Price'] = List[7]
priceList['Low Price'] =  List[9]
print(priceList)

driver.get("https://nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TATAMOTORS&illiquid=0&smeFlag=0&itpFlag=0")
content = driver.find_elements_by_class_name("stock")

price2 = ""
List2 = []

for i in content:
    price2 += i.text

List2 = list(map(str,price2.split("\n")))

priceList2 = {}

priceList2['Last Price'] = List2[0]
priceList2['Open Price'] = List2[5]
priceList2['High Price'] = List2[7]
priceList2['Low Price']= List2[9]

print(priceList)
print(priceList2)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", priceList = priceList , priceList2 = priceList2)

