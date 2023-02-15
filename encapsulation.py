# i the encpsulation we used get and set metod when u create object as run time
class stud:
    def __def__(self):
        self._name=""
    def getname(self):
        return self._name
    def sename(self,name):
        self._name=name
obj=stud()
obj1=stud()
obj.sename("Testing")
obj1.sename("devloper")

name=obj.getname()
print(name)
name=obj1.getname()
print(name)
