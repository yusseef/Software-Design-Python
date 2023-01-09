# Thats a one way to get and set another way is use property decorators instead
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # __ means private attributes

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

p1 = Person('yusseff', 11)
print(p1.getAge())


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # __ means private attributes
    
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name



#Usually python dont provide method overloading so we can't make two function with the same name but with setter decorator we can do that