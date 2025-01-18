class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        itr = self.head

        while itr is not None :
            print(itr.data,end="->")
            itr = itr.next

    def append(self,data):
        node = Node(data)
        itr = self.head
        if itr is None:
            self.head = node
            self.tail = node
        else :
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True
    def pop_first(self):
        temp = self.head
        if self.length == 0 :
            return None
        elif self.length == 1 :
            self.head = None
            self.tail = None
        else : 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1

    def pop(self):
        if self.length == 0:  # Case: Empty list
            return None
        
        temp = self.tail  # Save the current tail node
        
        if self.length == 1:  # Case: Single-node list
            self.head = None
            self.tail = None
        else:  # Case: Multiple-node list
            self.tail = self.tail.prev  # Move tail pointer backward
            self.tail.next = None  # Disconnect the old tail node
            temp.prev = None  # Disconnect temp from the list
        
        self.length -= 1  # Decrease the list length
        return temp
            



        



s = DoublyLinkedList()

s.append(25)
s.append(26)
s.append(27)
s.append(28)


s.print_list()

s.pop()
print("\n")
s.print_list()
print("\n")
s.pop_first()
s.print_list()

    





