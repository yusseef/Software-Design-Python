#singleton design pattern means that we have   class with only one object

class Person:
    __instance = None

    @staticmethod
    def get_instance():
        if Person.__instance is None:
            Person("Default")
        return Person.__instance

    def __init__(self, name):
        if Person.__instance != None:
            raise Exception("This class has alreadt an object")
        else:
            self.name = name
            Person.__instance = self
    @staticmethod
    def get_data():
        print(f"name {Person.__instance.name}")

p1=Person('Yussef')
print(Person.get_instance())
Person.get_data()