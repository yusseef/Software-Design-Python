#Dunder method is a method that begin  with two underscores like __init__

class Vector:
    def __init__(self, x, y): # ==> Dunder method
            self.x = x
            self.y = y

    def __add__(self, other): 
        return Vector(self.x + other.x, self.y + other.y) #SUM
    
    def __sub__(self, other): # =
        return Vector(self.x - other.x, self.y - other.y) #SUB

    def __mul__(self, other): 
        return Vector(self.x * other.x, self.y * other.y) #MUL

    def __str__(self): #Change how to print an object
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        print("Hello i was called")

v1 = Vector(50, 60)
v2 = Vector(100, 200) 
print(v1 * v2)
v1()