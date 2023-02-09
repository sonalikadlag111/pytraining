# Program to find the differences of two lists.

# list1 = [10, 20, 25, 45, 89, 90, 11]
# list2 = [23, 10, 34]
#
# list3 = []
# for element in list1:
#     if element not in list2:
#         list3.append(element)
#
#
# print(list3)

li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

temp3 = []
for element in li1:
    if element not in li2:
        temp3.append(element)

print(temp3)
