
from bs4 import BeautifulSoup
from urllib import request

# 주식 가격 읽어와서 데이터베이스에 저장해보자!
# https://finance.naver.com/item/sise.naver?code=005930

# 이 주소에서 데이터 가져올거야
url="https://finance.naver.com/item/sise.naver?code=003530"

#알려준 주소에서 코드 좀 다 읽어와바!
response= request.urlopen(url)
html = response.read()

# 가져온 코드의 구조를 분석해서 보유하자!
soup = BeautifulSoup(html, "html.parser")

#분석 결과 내에 내가 원하는 정보가 있다면 가져오자!
info = soup.select_one("#_nowVal")

price = info.text

import sqlite3

con= sqlite3.connect("database_stock.db")

cur= con.cursor()

cur.execute("INSERT INTO stocks VALUES(?,?)", ('한화투자증권', price))

con.commit()