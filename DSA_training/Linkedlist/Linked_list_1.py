class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end=" -> ")
            itr = itr.next
        print("None")  # End of the list

    def insert_value(self, data):
        node = Node(data)
        if self.length == 0:  # First node
            self.head = node
            self.tail = node
        else:
            self.tail.next = node  # Add the new node after the tail
            self.tail = node       # Update the tail to the new node
        self.length += 1  # Increment the length of the list

    def pop(self):

        if self.head is None :
            print("LinkedList is empty No POP")
            return
        if self.head.next is None :
            self.head = None
            self.tail = None
            self.length -= 1 
            return 


        temp = self.head
        pre = None

        while temp.next:  # Traverse until the last node
            pre = temp
            temp = temp.next

        # Remove the last node
        print(f"Popped value: {temp.data}")
        pre.next = None
        self.tail = pre  # Update the tail
        self.length -= 1  # Decrease the length

    def insert_at_begining(self,data):
         node =Node(data)
                
         if self.head is None :
            self.head = node
            self.tail = node
            self.length = 1
            return
         node.next = self.head
         self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None :
            self.insert_at_begining(data)
            return
        self.tail.next = node
        self.tail = node
        return True
    
    def insert_values_list(self,list):
        for i in list :
            self.insert_value(i)
        return
    

             

if __name__ == "__main__":        


# Example usage:
    s = LinkedList()
    t = LinkedList()
    k = LinkedList()
    s.insert_values_list([1,4])
    t.insert_values_list([3,2])

    s.print()
    t.print()

    itr = s.head
    itr2 = t.head
    while itr and itr2 :
        print(itr.data)
        print(itr2.data)
        sum =  itr.data + itr2.data
        k.insert_value(sum)

        itr = itr.next
        itr2 = itr2.next
    k.print()
