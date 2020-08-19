import folium

# map 클래스를 로드해서 초기 화면 설정
m = folium.Map(location=[37.559884, 126.945539],
               tiles="OpenStreetMap",
               zoom_start=15
               )

# marker 클래스를 이용하여 특정 위치를 아이콘으로 표시
marker1 = folium.Marker(location=[37.559884, 126.945539],
              tooltip='Ewha',
              icon=folium.Icon(color='green',icon='star')
             ).add_to(m)
marker2 = folium.Marker(location=[37.557176, 126.934947],
              tooltip='PieHole',
              icon=folium.Icon(color='green',icon='star')
             ).add_to(m)

# html 파일로 저장
m.save('map.html')