# Program to Create two lists with EVEN numbers and ODD numbers from a list.

list1 = [1, 2, 3, 4, 5]
listOdd = []
listEven = []
for num in list1:
	if num%2 == 0:
		listEven.append(num)
	else:
		listOdd.append(num)

print ("list1:    ", list1 )
print( "listEven: ", listEven)
print ("listOdd:  ", listOdd)
