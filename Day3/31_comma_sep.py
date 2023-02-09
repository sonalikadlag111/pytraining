# Input comma separated elements, convert into list and print.
str = str (input ("Enter comma separated integers: "))
print ("Input string: ", str)
list = str.split (",")
print ("list: ", list)
li = []
for i in list:
	li.append(int(i))

# print list as integers
print ("list is : ", li)
