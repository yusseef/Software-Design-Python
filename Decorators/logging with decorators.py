'''
Logging is track events happend when software runs 
in this case we will track the add values every time add() function runs
'''
def logged(func):

    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = func.__name__
            print(f'{fname} returned vallue {value}')
            f.write(f'{fname} returned vallue {value}')
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10, 50))
