# Python program to print positive or negative numbers in a list

myList = []
length = int(input("Enter number of elements : "))
for i in range(0, length):
    value = int(input())
    myList.append(value)

# printing all positive values of the list
print("All positive numbers of the list : ")
for aa in myList:
    if aa >= 0:
        print(aa, end=" ")
    # else:
        # print(aa,end="")
