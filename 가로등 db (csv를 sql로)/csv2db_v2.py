import pymysql
from sqlalchemy import create_engine
import csv
import pandas as pd
import pymysqldb

engine = create_engine("mysql+pymysqldb://root:"+"roguohry1"+"@localhost/ecb", encoding='utf-8')
conn = engine.connect()

with open('data/real_light_location.csv','r',encoding='UTF-8') as f:
    dr=csv.DictReader(f)
    df=pd.DataFrame(dr)
    df.columns = ['lat', 'lng']
# 이제 이 데이터프레임 df를 sql 파일로!!!!!1

'''
con = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='roguohry1',
    db='ecb'
)'''

df.to_sql(name='test_table', con=engine, if_exists='append')
'''
con.commit()
con.close()

    command = "a=Light(latitude_light="+lat+", longitude_light="+lng+")"
    os.system(command)
    os.system("a.save()")
'''
