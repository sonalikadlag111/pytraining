from functools import reduce

def add(x, y):
    return x + y

list = [2, 4, 7, 3]
print(reduce(add, list))