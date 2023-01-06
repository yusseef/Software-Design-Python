#Proxy design pattern used for preventing direct acces to methods
class Person:
    def __init__(self, name, age):
            self.name = name
            self.age = age
    def persondetails(self):
        return f'{self.name}, {self.age}'

class ProxyPerson(Person): #acts like a secondmane between user and class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.person = Person(name, age)

    def persondetails(self):
        print(f'{self.name}, {self.age} from proxy design pattern')

p1 = ProxyPerson('yusse', 23)
print(p1.persondetails())
