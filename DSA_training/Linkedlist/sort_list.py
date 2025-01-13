from Linked_list_1 import *

s = LinkedList()
t = LinkedList()

s.insert_values_list([2,4,3])
t.insert_values_list([5,6,4])

s.print()
t.print()

itr1 = s.head
itr2 = t.head 
itr_str = ""
itr_str2 = ""


while itr1 and itr2  :
    itr_str = str(itr1.data) + itr_str
    itr_str2 = str(itr2.data) + itr_str2

    itr1 = itr1.next
    itr2 = itr2.next

