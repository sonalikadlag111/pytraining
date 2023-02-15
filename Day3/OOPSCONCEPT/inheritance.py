# multilevel Inhertance

class a:
    b=40


    def displayA(self):
        self.b=self.b
        print(self.b)

# inherit a in to b single inheritance
class b():
    def displayB(self):
        print("welcome BBB")

class c():
    def displayC(self):
        print("welcome to CCC")
    def __init__(self):
        print("dfdsfdf")

# obj=b()
obj=a()
obj2=b()
obj3=c()
obj.displayA()

obj2.displayB()
obj3.displayC()






