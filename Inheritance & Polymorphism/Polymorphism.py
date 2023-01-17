class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def good_boy(self):
        return True

    def bark(self):
        return 'Hoof'


class Golden(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def color(self):
        return 'Golden color'

    def bark(self):
        return 'Arf Arf'

class Haskey(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def feather(self):
        return 'Heave hair'

    def bark(self):
        return 'Wooaah'

class Holden(Haskey, Golden):
    def __init__(self, name, age):
        super().__init__(name, age)


doggy = Dog('Normal',1)
goldie = Golden('Goldie',1)
haskey = Haskey('7az2a', 2)
holden = Holden('holdie', 3)
print(doggy.bark())
print(goldie.bark())
print(haskey.bark()) #takes first base class method
print(holden.bark())

