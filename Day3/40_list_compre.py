# Python program to remove multiple elements from a list using list comprehension


list1 = [10, 20, 30, 40, 50, 60, 70]
print("The list is: ")
print(list1)

indices = 0, 2, 4,5,1
list1 = [i for j, i in enumerate(list1) if j not in indices]

print("After removing elements, list is: ")
print(list1)
