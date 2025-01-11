

class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


current = node1

while current is not None:
    # print(current)
    print(current.data,end="-->")

    current = current.next
    if  current.next == None :
        exit()

    
# print(node4.next)


# current 1 --> 10 - location
    # current 2 --> 20 location  


