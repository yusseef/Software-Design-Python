def generator(n):
    for x in range(n):
        yield x ** 3 #Yield return value and when executed again it returns the next value

values = generator(500)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
