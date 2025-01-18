class Node :
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):   
        self.head = None
        self.tail = None 
        self.length = 0

    def print(self):
        itr = self.head
        while itr :
            print(itr.value,end="->")
            itr = itr.next
    def insert_values(self,value):
        node =  Node(value)
        if self.head is None :
            self.head = node
            self.tail = node
            self.length = 1
        
        itr = self.head
        while itr :
            itr = itr.next
        self.tail.next = node
        self.tail = node
        node.next = None
        self.length  += 1 




s =  LinkedList()

s.insert_values(10)

s.insert_values(11)



s.print()
        
        



