class EmailAddress:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        #print('get is called')
        return self._name

    @name.setter
    def name(self, name):
        #print('set is called')
        self._name = name

    @property
    def email(self):
        #print('get is called')
        return self._email

    @email.setter
    def email(self, name):
        #print('set is called')
        self._email = name

    def display_all(self):
        print('NAME: ', self.name)
        print('EMAIL: ', self.email)
        

###########################################################################
        
##one = propertygetset.EmailAddress('IJ','ij@gmail.com')
##
##print(one.name)
##print(one.email)
##
##one.name = 'SJ'
##one.email = 'sj@gmail.com'
##
##one.display_all()



