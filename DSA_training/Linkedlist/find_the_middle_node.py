class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    def print(self):
        itr = self.head
        while itr :
            print(itr.value,end="->")             
            itr = itr.next

    def find_mid_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow
          

    




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.print()

s = my_linked_list.find_mid_node()
print(s.value)

"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""