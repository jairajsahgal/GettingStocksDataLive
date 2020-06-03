import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
import time as waqt
import random
def real_time_price(stock_code):
	url = ('https://finance.yahoo.com/quote/')+stock_code+('?p=')+('&.tsrc=fin-srch')
	r=requests.get(url)

	web_content=BeautifulSoup(r.text,'lxml')
	web_content=web_content.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})

	web_content=web_content.find('span').text
	if web_content==[]:
		web_content='99999'
	return web_content

HSI=['^NSEI','^DJI','^NYA','^GSPC']

for step in range(1,101):
	price=[]
	col=[]
	waqt.sleep(random.randint(10,15))
	time_stamp=datetime.datetime.now()
	time_stamp=time_stamp.strftime("%Y-%m-%d %H:%M:%S")
	for stock_code in HSI:
		price.append(real_time_price(stock_code))
	col=[time_stamp]
	col.extend(price)
	df=pd.DataFrame(col)
	df=df.T
	df.to_csv("realtimestockdata.csv",mode='a',header=False)
	print(col)

