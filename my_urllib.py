import urllib.request
import json

x = urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") #json file

print(x)
print(type(x))

for line in x:
    print(line)

x = urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") #json file
y = json.loads(x.read().decode('utf-8'))[:10]

print(y[3]['name'],y[3]['id'],y[2]['address']['city'])
