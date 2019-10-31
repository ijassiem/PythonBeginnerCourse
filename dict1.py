dict = { '1':'apple','2':'banana','3':'orange','4':'pear'}

print(dict)
print(dict.items())

for x in dict.keys():
    print(x)

for x in dict.values():
    print(x)

for key, val in dict.items():
    print (key, val)
