class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def good_boy(self):
        return True


class Golden(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def color(self):
        return 'Golden color'

class Haskey(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def feather(self):
        return 'Heave hair'

class Holden(Golden, Haskey):#multiple inheritance
    def __init__(self, name, age): 
        super().__init__(name, age)



golden = Golden('Godlie', 2)
haskey = Haskey('Haskey', 1)
holden = Holden('Holden',3)

print(golden.color())
print(haskey.feather())
print(holden.color())
print(holden.feather())
print(holden.good_boy())




