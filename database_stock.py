
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

# MYSQL 같은모듈, 파이썬에 기본 내장된 데이터베이스시스템
import sqlite3

# 전제: 이 파이썬 파일과 같은 폴더 내에 .db 파일이 하나 존재한다!

# 이 파이썬 파일과 데이터베이스 파일을 연결하여 작업 가능하게 만든다!
con= sqlite3.connect("database_stock.db")

# 연결이 되었다면, 연결된 파일에 sql 구문을 전달해서 실행할 객체를 생성해야한다!
cur= con.cursor()

# 테이블 생성 명령 실행
# cur.execute("CREATE TABLE customer(name TEXT, age INT)") #테이블이 생성되면 더이상 작동하지않는다
cur.execute("INSERT INTO stocks VALUES(?,?)", ('한화투자증권', price))

con.commit()