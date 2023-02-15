# overloading same function but argument are diff

class Area:
    def find_Area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing")
obj=Area()
obj.find_Area()
obj.find_Area(10)
obj.find_Area(10,20)
