class Room(object):
    # def __init__(self):
    #     self.length = 0
    #     self.breadth = 0

    def calculate_area(self,length,breath):
        self.length = length
        self.breadth = breath
        print("Area of room :", self.length * self.breadth)


room1 = Room()
room2 = Room()

room1.calculate_area(10, 10)
