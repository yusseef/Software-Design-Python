from abc import ABC, abstractmethod

class Person(ABC):
    
    @abstractmethod
    def type(self):
        pass

class Student(Person):
    def type(self):
        return "Student"

s1 = Student()
print(s1.type())


def generator(n):
    for i in range(n):
        yield i

values = generator(500)
