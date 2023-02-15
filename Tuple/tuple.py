t=(10,20,30,40,50)
t[2]
print(t)
print(type(t))
# dicstionary iterater
t1=len(t)
print(t1)
for i in range(t1):
    print(t[i])
m=min(t)
print(m)
m=max(t)
print(m)
c=t.count(10)
print(c)
i=t.index(10)
print(i)

q=t[3]
print(q)
s=sum(t)
print(s)