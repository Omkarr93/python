class A:
    def __init__(self):
        print("This is init in Class A")

    def feature1(self):
        print("The feature 1 class A")
    def feature2(self):
        print("The feature 2 class A")

class B:
    def __init__(self):
        print("this is init in class B")

    def feature1(self):
        print("The feature 3 class B")
    def feature4(self):
        print("the feature 4 class B")

class C(B,A): 
    def __init__(self):
        super().__init__()
        print("this is init in C ")
    


a1 = B()
aC = C()

aC.feature1()



