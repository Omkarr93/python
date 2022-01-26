class  computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config (self):
       print("config is ",self.cpu,self.ram)



comp1 = computer('i5',16)
comp2 = computer('i10',8)

# computer.config(comp1)
# computer.config(comp2)

# comp1.config()
comp2.config()