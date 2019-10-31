class EmailAddress:
    def __init__(self, name, surname, email = 'default'):
        self.name = name
        self.surname = surname
        self.email = email

    @property
    def get_email(self):
        return self.name.casefold() + '.' + self.surname.casefold() + '@webmail.com'

    @get_email.setter
    def get_email(self, name):
        self.email = name
        

    @property
    def get_fullname(self):
        return self.name + ' ' + self.surname


one = EmailAddress('Ismail','Jassiem')
print(one.name)
print(one.surname)
print(one.get_email)
print(one.get_fullname)
one.name = "Mike"
one.get_email = "ismjas@gmail.com"
print(one.name)
print(one.surname)
print(one.get_email)
print(one.get_fullname)




