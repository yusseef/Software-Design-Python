class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('yusseff', 23)
print(p1.name)

'''
    in this example any one can access the attributes of the class cause its public
    and this against encapsulaltion so we need to make it private and use setters and getters. 
'''