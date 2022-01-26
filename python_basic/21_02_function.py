def greet(name):
    print('Have a good day,'+name)

def sumfunction(num1,num2):
    return num1 +num2    
# factorial - 1*2*3*4*5*n           n*(n-1)!  #5*(5-1)
def factorial_recurssive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recurssive(n-1)     


f = factorial_recurssive(5)
print(f)




greet('omkar')
greet('Shri')
greet('Priyanka')

a=sumfunction(56, 25)
print(a)
