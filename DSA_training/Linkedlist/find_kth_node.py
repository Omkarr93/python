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
  
        
    def find_kth_from_end(self,ls,k):
        slow = self.head
        fast = self.head
        

        for _ in range(k):
           if not fast :
                return None
           fast = fast.next
        while fast :
            fast = fast.next
            slow =  slow.next
        return slow.value
    









my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.print()
k = 1
result = my_linked_list.find_kth_from_end(my_linked_list,k)

print("\n",result)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

