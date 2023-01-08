#Decorators is used to extend a function's behaviour
#This is the default decorator syntax but in python we can do it in another way 
def decorator(func):

    def wrapper():
        func()
        print("i,m from decorator")
    return wrapper

def hello():
    print('Hello')
decorator(hello)()
