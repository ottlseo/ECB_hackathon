
import csv
import os
import pandas as pd
import sqlite3

with open('data/real_light_location.csv','r',encoding='UTF-8') as f:
    dr=csv.DictReader(f)
    df=pd.DataFrame(dr)
    df.columns = ['lat', 'lng']

######### 여기까진 수정할 거 없음 ###########
# 이제 이 데이터프레임 df를 sql 파일로!!!!!1

con = sqlite3.connect('../db.sqlite3')
cursor = con.Curs #커서 설정
# 이제 이 커서와 df를 이용 -> to_sql 함수에 넣기

df.to_sql('light_db', cursor, index=True)
con.commit()