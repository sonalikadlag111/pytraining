# Python program to print list elements in different ways.
a = [1, 2, 3, 4, 5]
print(*a)

print("printing lists separated by commas")

print(*a, sep = ", ")


print("printing lists in new line")

print(*a, sep = "\n")

list1 = ["Amit", "Abhi", "Radib", 21, 22, 37]
list2 = [100, 200, "Hello", "World"]

print(list1)
print(list1[0])
print(list1[0], list1[1])
print(list1[2:5])
print(list1[1:])
print(list2 * 2)
print(list1 + list2)
