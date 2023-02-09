# 08. Program to Subtract a List from Another List substraction zip()

a=[10,4,6,7]
b=[8,5,13,5]
sub=[]
for i ,j in zip(a,b):
    sub.append(i-j)
print(sub)




