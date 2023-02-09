# Remove falsy values from a list in Python

# Remove falsy values from a list in Python
def newlist(lst):
  return list(filter(None, lst))

# main code
list1 = [10, 20, 0, 30, 0, None]
list2 = [40, False, "Hello", "", None]
list3 = [False, None, 0, "", "Hello", 10, "Hi!"]

# printing original strings
print("list1: ", list1)
print("list2: ", list2)
print("list3: ", list3)

# removing falsy values and printing
print("newlist(list1): ", newlist(list1))
print("newlist(list2): ", newlist(list2))
print("newlist(list3): ", newlist(list3))
