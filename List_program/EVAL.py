# An exception will be raised
# from math import *
# exec("print(factorial(5))", {})

# for num in range(6):print(num,num**2,num**3)
# exec(code)
#
# def decor(func):
#     def wrap():
#         print("sdfdsdds")
#         func()
#         print("sdfdsdcsdcscsdds")
#     return wrap
#
# def sayHello():
#     print("hello")
# newfunc=decor(sayhello)
# newfunc()

# myfunc=decorator(divide)
# myfunc(2,3)

# def fun1():
#     print("sub noe")
# fun2=fun1
# del fun1
# fun2()

def(func1):
 def nowexec():
        print("executing this")
        func1()
        print("exicuted")
    return nowexec
@dec1
def who_is_harry():
    print("harry is good boy")
# who_is_harry=dec1(who_is_harry)

who_is_harry()