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
            self.prev = self.tail
            self.tail = node
        self.length += 1
        return True
        



s = DoublyLinkedList()

s.append(25)
s.append(26)

s.print_list()

    





