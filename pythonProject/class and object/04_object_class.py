class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
      print('The config of ',self.cpu,',',self.ram)
      print(" Yeahhhh ")
    def compare(self,other):
        if self.ram > other.ram:
         return True
        else:
            False 

         
comp1 = computer('I5',25)
comp2 = computer('rayzen',16)

comp1.config()
comp2.config()


if comp1.compare(comp2):
    print('The ram of comp1 is greater')
else:
    print("Not greater")    
 