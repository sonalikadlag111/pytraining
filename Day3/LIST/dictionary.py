# d={
#     'name':'sonali',
#     'address':'pune',
#     'email':'sonali@gmail.com'
# }
# # print(d)
# # n=d['name']
# # print(n)
# # for i in d:
# #     print(d[i])
# #     get
# n=d.get('name')
# print(n)
# n=d.get('address')
# print(n)
#
# # keys
#
# for i in d.keys():
#     print(i)
# for i in d.values():
#     print(i)
# for i,j in d.items():
#     print(i,j)
# del d['email']
# print(d)
# a=d.pop('name')
# print(a)
# print(d)
#
course={
    'php':{'duration':'6month','fess':4000},
    'java':{'duration':'3moths','fess':4000},
    'py':{'duration':'3moths','fess':4000},}

# print(course)
# print(course.get('php'))
# print(course.keys('java'))
# for i in course.keys():
#     print(course[i])
# for i in course.pop('java'):
#     print(i)
# for i,j,k in course.items():
    # print(i,j,k)
course['php']['fess']=100000
print(course)

