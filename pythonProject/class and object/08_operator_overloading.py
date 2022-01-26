# Polymorphism
class student:
    def __init__(self,m1,m2):
         self.m2 = m2 
         self.m1 = m1
    
    def total(self):
        to = self.m1 + self.m2
        print(self.m1,self.m2,to)
   

std1 = student(47, 48)
std2 = student(54, 84)
std3 = student(95, 84)
std4 = student(25, 84)
std5 = student(87, 84)
std6 = student(25, 84)
std7 = student(95, 84)
std8 = student(65, 84)
std9 = student(25, 95)
std10 = student(25, 58)
std11 = student(58, 95)

std1.total()

