class Person:
    def __init__(self, name, age):
            self.name = name
            self.age = age
    def persondetails(self):
        return f'{self.name}, {self.age}'

p1 = Person('Yussef', 23)
print(p1.persondetails())