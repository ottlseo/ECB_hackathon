import folium

coordinates = [
               [37.559894, 126.945482],
               [37.562117, 126.949126],
               [37.563662, 126.946819],
               [37.566478, 126.948406]
              ]

# Create the map and add the line
ave_lat = sum(p[0] for p in coordinates)/len(coordinates)
ave_lon = sum(p[1] for p in coordinates)/len(coordinates)

m = folium.Map(location=[ave_lat, ave_lon],
               tiles="OpenStreetMap",
               zoom_start=15
               )

marker1 = folium.Marker(location=[37.559894, 126.945482],
              tooltip='정문',
              icon=folium.Icon(color='green',icon='flag')
             ).add_to(m)
marker2 = folium.Marker(location=[37.562117, 126.949126],
              tooltip='중앙도서관',
              icon=folium.Icon(color='green',icon='flag')
             ).add_to(m)
marker3 = folium.Marker(location=[37.563662, 126.946819],
              tooltip='포스코관',
              icon=folium.Icon(color='green',icon='flag')
             ).add_to(m)
marker4 = folium.Marker(location=[37.566478, 126.948406],
              tooltip='아산공학관',
              icon=folium.Icon(color='green',icon='flag')
             ).add_to(m)

path = folium.PolyLine(
                        locations=coordinates,
                        color='pink',
                        weight=5
                      ).add_to(m)

# html 파일로 저장
m.save('map.html')