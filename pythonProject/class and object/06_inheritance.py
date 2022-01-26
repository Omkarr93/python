class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("Feature 2 is working") 

class B(A):                 #inhertance of values from class A
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

A1 = A()
b1= B()
A1.feature1()
A1.feature2()
b1.feature1()    #inheritance of values from class A 



