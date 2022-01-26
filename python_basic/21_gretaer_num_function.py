def Greaternum (a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c    

    
a= Greaternum(58 , 100, 27)
print("The greatest number is",str(a))