def diamond ():


 n=5
 for i in range(n-1):
    for j in range(i,n-1):
     print('  ',end='')
    for j in range((i+1)-1):  #upper triangle
     print('# ',end='')
    for j in range(i+1):
     print('#',end=' ')  
    print()
 n=5
 for i in range (n):
    for j in range(i):
     print(' ',end=' ')
    for j in range((n-i)-1):   #lower
     print('#',end=' ')
    for j in range(i,n):
     print('#',end=' ')  
    print()    


diamond()
diamond()
# print(a,end='')
# print(b,end='')
