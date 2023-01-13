import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json

count = 0
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


address = input('Enter location: ')
while len(address) < 1:
    break
print('Retrieving', address)
uh = urllib.request.urlopen(address)
da = uh.read()

'''data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
stuff = ET.fromstring(data)
lst = stuff.findall('comments')'''

info = json.loads(da)
for i in info["comments"]:
    num = int(i["count"])
    count += num


print(count)
