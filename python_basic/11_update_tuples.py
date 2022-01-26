# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
a= (34,56,78,4,'omkar',True,45.6)
b=(43,25,'Omkar')            
y =list(a)
y.pop(6)
a=tuple(y)
# y.pop(7)
# a= tuple(y)
print(a)
# del a         deletess the tuple completly
print(a)
# print(a)
# print(type(a))
# y = list(a)
# # print(type(y))
# y.insert(1, 12)
# print(y)
# a= tuple(y)
# print(a)
# print(type(a))

# Y = list(a)
# print(type(Y))