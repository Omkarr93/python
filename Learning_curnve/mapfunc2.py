def splicer(mystring) :
    if len(mystring) % 2 == 0 :
     return 'EVEN'
    else :
       return mystring[0]
    

names = ['andy','eve2','sally']
value =  list(map(splicer,names))

print(value)