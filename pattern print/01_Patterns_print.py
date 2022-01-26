# for j in range(4):
#  for i in range(4):
#         print('# ',end='')

#  print()

n = 5

for i in range(n - 1):
    for j in range(i):
        print(' ', end=' ')
    for j in range((n - i) - 1):  # lower
        print('#', end=' ')
    for j in range(i, n):
        print('#', end=' ')
    print()

n = 5
for i in range(n):
    for j in range(i, n - 1):
        print('  ', end='')
    for j in range((i + 1) - 1):  # upper triangle
        print('# ', end='')
    for j in range(i + 1):
        print('#', end=' ')
    print()
# n=5    
# for i in range (n):
#       for j in range(i):
#        print(' ',end=' ')
#       for j in range((n-i)-1):   #lower triangle
#         print('#',end=' ')
#       for j in range(i,n):
#         print('#',end=' ')  
#       print()


# for j in range(i):
#   print()


# for j in range(4):
#  for i in range(4-j):
#         print('# ',end='')


#  print()
