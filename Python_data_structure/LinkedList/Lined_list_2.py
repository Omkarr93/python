class Node :
   def __init__(self,data):
      self.data = data
      self.next = None



node1 = Node(10)
node2 =  Node(20)
node3 =  Node(30)
node4 =  Node(40)
node5 =  Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# add node to start 
head = node1
new_node = Node(5)
new_node.next = head
head = new_node



current =  head

while current is not None:
    print(current.data,end="-->")

    current = current.next








    