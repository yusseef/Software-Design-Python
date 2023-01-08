def decorator(func):
    def wrapper(*args, **kwargs):
        print('I,m from decorator')
        func(*args, **kwargs)
    return wrapper

@decorator #Annotation decorator
def hello(name):
    print(f'hello {name}')

hello('yussef')