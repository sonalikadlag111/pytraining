# multilevel Inhertance

class a:
    def displayA(self):
        print("welcome AAA")

# inherit a in to b single inheritance
class b(a):
    def displayB(self):
        print("welcome BBB")

class c(b):
    def displayC(self):
        print("welcome to CCC")


# obj=b()
obj=c()
obj.displayA()
obj.displayB()
obj.displayC()

