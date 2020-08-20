import sqlite3
a=36.444
b=38.444
c=126.953
d=126.954

conn = sqlite3.connect("light.db")
cur = conn.cursor()
cur.execute("SELECT * FROM real_light_location WHERE latitude>%f AND latitude<%f AND longitude>%f AND longitude<%f;"%(a,b,c,d))
             # 위도 경도 값이 범위 내인 가로등 데이터를 추출
print(cur.fetchall()) # 추출한 데이터 모두를 리스트 형태로 print

conn.commit() # 변경 내용 저장
conn.close() # db 닫기