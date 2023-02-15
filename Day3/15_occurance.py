# Program to remove first occurrence of a given element in the list.
list = [14, 220, 14, 30, 14, 40, 14, 50,14]
n = 14
ans=[i for i in list if i!=n]
print(ans)

ans1=[m for m in list if m!=n]
print(ans1)


# ans1=[i for i in list if i==n]
# print(ans1)