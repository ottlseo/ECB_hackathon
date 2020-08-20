import pymysql

import csv
import pandas as pd

con = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='roguohry1',
    db='ecb'
)
cursor = con.cursor() #커서 설정
namelist = ['윤가영','한근영','김서현','김채연','문아영','제발돼랑']

for i in range(5):
    thisname = str(namelist[i])
    thisage = int(i)
    query = '''INSERT INTO ecb_test (name, age) VALUES(thisname, thisage);'''
    cursor.execute(query)
con.commit()
con.close()