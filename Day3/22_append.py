# Program to input, append and print the list elements.

list=[]
n=int(input("enter the no of limit to list :"))
for i in range(n):
    item=int(input("enter the any integer :"))
    list.append(item)
print("element are :")
for i in range (n):
        print(list [i])