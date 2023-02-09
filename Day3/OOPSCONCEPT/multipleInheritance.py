# multiple inheritance

class A:
    def displaya(self):
        print("welcome")

class B:
    def displayb(self):
        print("to the")

class C(A,B):
    def displayc(self):
        print("baap")

obj=C()
obj.displaya()
obj.displayb()
obj.displayc()
