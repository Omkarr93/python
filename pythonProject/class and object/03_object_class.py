class computer:
    def __init__(self):
        self.name = 'Omkar'
        self.age = 23
    def update(self):
        self.age = 30    
    def compare (self,other):
        if self.age == other.age:
          return True
        else:
          return False 
    


c1  = computer()
c2 = computer()

print(c1.name,c1.age)
print(c2.name,c2.age)


c1.update()

if c1.compare(c2):
    print('They are same')
else :
    print("Not same")







# print(id(c1))
# print(id(c2))