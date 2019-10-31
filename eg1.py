import propertygetset # imports class named 'EmailAddress' in 'propertygetset.py'
     
one = propertygetset.EmailAddress('IJ','ij@gmail.com')

print(one.name)
print(one.email)

one.name = 'SJ'
one.email = 'sj@gmail.com'

one.display_all()




