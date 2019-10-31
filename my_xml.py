import urllib.request
import json

x = urllib.request.urlopen("https://www.ledge.co.za/album.xml") #xml file

for line in x:
    print(line)
