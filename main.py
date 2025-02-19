import folium

centro = [25.674453699177754, -100.21357677942221]
m = folium.Map(location=centro, zoom_start=12)
m.save('index.html')

