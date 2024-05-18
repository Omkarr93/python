# add node at end of linked list 

class Node :
    def __init__(self,data) :
        self.data = data
        self.next =  None



node1 = Node(10)
node2 =  Node(20)
node3 =  Node(30)
node4 =  Node(40)
node5 =  Node(50)


#linking nodes 

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


new_node = Node(60)
head = node1
current = head

while current is not None:
    current = current.next

  
current = new_node


