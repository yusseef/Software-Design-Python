#This decorator calculate the time need to execute a function 
import time
def time_needed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        fname = func.__name__
        print(f'{fname} function took {after - before} to execute')
        return value
    return wrapper

@time_needed
def add(x, y):
    return x + y

print(add(10, 20))

