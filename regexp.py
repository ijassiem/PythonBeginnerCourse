import re

x = re.search('hello', 'hello world')
print(x)
x = re.search('h.*o', 'hello world')
print(x)
x = re.search('h.*?o', 'hello world')
print(x)
if re.search('h.*?so', 'hello world'):
    print('Matched')
else:
    print('No match')

IP_REGEX = r'(\d{1,3}\.){3}\d{1,3}'

x = re.search(IP_REGEX, '192.168.1.1')
print(x)

EMAIL_REGEX =r'[\w.-]+@[\w.-]+\.[a-z]{1,20}'

x = re.search(EMAIL_REGEX, 'my email is ijassiem@ska.ac.za')
print(x)

EMAIL_REGEX2 =r'([\w.-]+)@([\w.-]+\.([a-z]{1,20}))'

x = re.search(EMAIL_REGEX2, 'my email is ijassiem@ska.ac.za and ismjas@gamil.com')
print(x)
print(x.groups())

x = re.findall(EMAIL_REGEX2, 'my email is ijassiem@ska.ac.za and ismjas@gamil.com')
print(x)

for match in re.finditer(EMAIL_REGEX, subject):
    print(

