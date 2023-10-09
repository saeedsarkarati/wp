import folium
m = folium.Map(location=[36, 50], zoom_start=20)
# ~ m = folium.Map(location=[40.05000, 41.6238])
# ~ m = folium.Map(location= [41.6238, 40.05000],
                    # ~ zoom_start=20,
                    # ~ crs='EPSG4326') 
m.save("index.html")
print (type (m))
