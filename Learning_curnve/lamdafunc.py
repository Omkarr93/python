# square = lambda num : num ** 2

my_num = [1,2,3,4,5]

# for i in map(square,my_num) :
returned = set(map(lambda num : num **2,my_num))
print(returned)