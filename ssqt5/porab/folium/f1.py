import folium
m = folium.Map(location=[45.5236, -122.6750])
m.save("index.html")
import io
from PIL import Image

img_data = m._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('image.png')
