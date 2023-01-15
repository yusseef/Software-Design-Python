#Multithreading means run more than one function togethersharing the memory
import threading

def function1():
    for i in range(50):
        print("Function1")

def function2():
    for i in range(50):
        print("Function2")


t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()

t1.join() #make the threading ended first before the rest of code executed