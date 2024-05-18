
class Node:
    def __init__(self,data,next=None) :
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head =  node

    def print(self):
        if self.head is  None:
            print('Linked list is empty')
            return
        itr = self.head

        pstr = ""
        while itr :
            pstr += str(itr.data) + '-->'
            itr = itr.next
        print(pstr)

    def insert_at_end(self,data):
        if self.head is None :
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        
        if self.head is None:
         for data in data_list:
            self.insert_at_end(data)
        else :
            itr =  self.head
            while itr is not None :
                itr = itr.next
            
            for data in data_list:
             self.insert_at_end(data)
    def get_length(self):
        count = 0 
        itr =  self.head
        while itr :
            itr = itr.next
            count += 1
        return count
    def remove_at(self,index):
        if index < 0 or index >= self.get_length() :
            raise Exception("This is not a valid index")
        if index ==0 :
            self.head = self.head.next
        count = 0
        itr =  self.head 
        while itr :
            if count == index -1 :
                itr.next = itr.next.next
                break
            
            itr =  itr.next
            count += 1

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length() :
            raise Exception("This is not a valid index")
        if index == 0 :
            self.insert_at_begining(data)
            return
        count = 0
        itr =  self.head 
        while itr :
            if count == index -1 :
                node = Node(data, itr.next)
                itr.next = node
                break
            itr =  itr.next
            count += 1
        



        


        


s =  Linkedlist()
s.insert_at_begining(10)
s.insert_at_begining(20)
s.insert_at_begining(30)
s.insert_at_end(800)
s.insert_values(['apple','bannana','jackfurit','orange'])
# print(s.head.data)
# print(s.get_length())
s.print()
# s.remove_at(20)
s.print()
s.insert_at(4,"Omkar")
s.print()




