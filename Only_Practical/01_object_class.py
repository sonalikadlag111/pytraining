# # object and classes
# class Parrot:
#
#     # class attribute
#     name = ""
#     age = 0
#
# # create parrot1 object
# obj = Parrot()
# obj.name = "Blu"
# obj.age = 10
#
# # create another object parrot2
# parrot2 = Parrot()
# parrot2.name = "Woo"
# parrot2.age = 15
#
# print(obj.name,obj.age)
# print((f"{parrot2.name}is{parrot2.age} years old"))

class dog:
    name1=""
    address=""
    age=0
class cat:
    n=""
    address1=""
    age1=0


obj1=cat()
obj1.n="manu"
obj1.age1=9
obj1.address1="mumbai"

obj2=cat()
obj2.n="mikky"
obj2.age1=4
obj2.address1="USA"
print(f"my name is {obj2.n} i am {obj2.age1} years old and my address is {obj2.address1}")
print(f"my name is {obj1.n} i am {obj1.age1} old and my adress is {obj1.address1}")


obj=dog()
obj.name1="duguu"
obj.age=12
obj.address="pune"

print(f"my name is {obj.name1} and my age is {obj.age} and my adress is {obj.address}")