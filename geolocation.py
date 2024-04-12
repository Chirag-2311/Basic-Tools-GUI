import geocoder
import folium
import socket
import sys

domain = sys.argv[1]
ip = socket.gethostbyname(domain)

g = geocoder.ip(ip)
myaddress = g.latlng
print(myaddress)
myMap = folium.Map(location=myaddress, zoom_start=12)
folium.Marker(myaddress, popup="My Location").add_to(myMap)
folium.CircleMarker(myaddress, radius=50, color='red',
fill_color='red').add_to(myMap)
myMap.save("mylocation.html")