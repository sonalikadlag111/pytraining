# Program to remove duplicate elements from the list.
mylist = [1,1,3,4,3,5,6,7]
mylist = list(dict.fromkeys(mylist))
print(mylist)