import folium
import pandas

df = pandas.read_csv('light_location.csv')
df.head()

map = folium.Map(location=[37.559884, 126.945539],
               tiles="OpenStreetMap",
               zoom_start=15
               )
for i in df.index[:770]:
    folium.Marker(location=df.loc[i, ['longitude', 'latitude']],
                  tooltip=df.loc[i, 'num'],

                  icon=folium.Icon(color='green', icon='star')
                  ).add_to(map)

map.save('map.html')