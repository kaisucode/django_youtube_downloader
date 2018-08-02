
import threading
from threading import Thread

def func1():
    for i in range(0, 20, 2): 
        print (i)

def func2():
    for i in range(0, 20, 2): 
        print (i)

if __name__ == '__main__':
    Thread(target = func1()).start()
    Thread(target = func2()).start()

