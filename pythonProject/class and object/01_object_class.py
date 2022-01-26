class comp :
        def __init__(self):
            print('Hello_world')
                
        def config(self):              # config is method
            print('Omkar')

comp1 = comp()                           # comp1 is known as object
comp2 = comp()

comp.config(comp1) 
comp.config(comp2)
comp1.config()
comp2.config()
