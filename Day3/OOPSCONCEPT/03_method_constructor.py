class demo:
    a=10


    def add(self):
        print(self.a)
        self.c=self.a*self.a
        print(self.c)
    def div(self):
        print("welcome")
    def div2(self,a,b):
        print(a+b)
        # constuctor
    def __init__(self):
        print("welcome to the baap")



obj=demo()
obj.add()
obj.div()
obj.div2(40,50)
