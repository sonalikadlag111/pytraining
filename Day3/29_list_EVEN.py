# print list after removing EVEN numbers.
list = [11, 22, 33, 44, 55, 4, 67, 2]
for i  in list:
    if(i%2 == 0):
        list.remove(i)
print ("list after removing EVEN numbers:")
print( list)
