
# Program to print all numbers which are divisible by M and N in the List

list = [10, 15, 45,21,10,20, 25, 30]
M = int(input("enter m :"))
N = int(input("enter n :"))
print ("List is: ", list)
print("Numbers divisible by m and n".format (M, N))
for num in list:
	if( num%M==0 and num%N==0 ):
		print (num)
