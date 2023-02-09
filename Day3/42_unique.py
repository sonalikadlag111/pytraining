# Check all elements are unique or not in Python  cant understand

def check_unique(x):
  return len(x) == len(set(x))

# lists
x = [10, 20, 30, 40,50]
y = [10, 20, 20, 20, 20]
z = [10, 10, 10, 10, 10]

print("x: ", x)
print("len(x): ", len(x))
print("set(x): ", set(x))
print("len(set(x)): ", len(set(x)))
print("check_unique(x): ", check_unique(x))
print()