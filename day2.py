class Person:

    def __init__(self):
        self.name = "Ismail"
        self.age = 2

    def talk(self):
        print("My name is ", self.name)

    def walk(self):
        if self.age <=1:
              print("Crawl")
        elif self.age > 1 and self.age < 60:
              print("Walk with 2 legs")
        else:
              print("Walk with stick")
              
####################################################################
              
class Friend:

    def __init__(self, name ='',age=0.0):
        self.name = name # instance variable
        self.age = age # instance variable

    def talk(self):
        print("My name is ", self.name)

    def walk(self):
        if self.age <=1:
              print("Crawl")
        elif self.age > 1 and self.age < 60:
              print("Walk with 2 legs")
        else:
              print("Walk with stick")
###################################################################
              
class Employee(Person):

    def __init__(self):
        super().__init__()
        self.rank = 'Grade B'

    job = 'Engineering' # class variable

    def work(self):
        print("My job is", self.job)
###################################################################
        
test = Person()
test.talk()
test.walk()

testy = Friend("Mr Jassiem")
testy.talk()
testy.walk()

testo = Employee()
testo.work()
testo.talk()



        
