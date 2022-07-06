# ip address locator 
# made by Abhishek Kumar Sahu @themodernhacker

import geocoder as geo

ip_address = geo.ip('me')
print(ip_address)

# find city of ip

ip = geo.ip('192.xxx.xxx.x')
print(ip.city)

# get latitude and longitude of ip address
print(ip.latlng)

# get area information

info = geo.google('San Francisco') # any area name according to your choice !!!
print(info.geojson)
print(info.osm)
print(info.wkt)

# You can also Follow Me on Social Media:-

# LinkedIn - https://linkedin.com/in/themodernhacker/

# Facebook - https://facebook.com/TheModernHacker/

# Twitter - https://twitter.com/TheModernHacker/

# Instagram - https://www.instagram.com/themodernhacker