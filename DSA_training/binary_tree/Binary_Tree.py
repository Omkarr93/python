class Node :
     def __init__(self,value):
          self.value = value
          self.right = None
          self.left = None

class BinarySearchTree :
     def __init__(self):
          self.root = None

     def insert(self,value):
          new_node = Node(value)

          if self.root  is None :
               self.root = new_node

          temp = self.root

          while True :
               if new_node.value == temp.value :
                    return False
               if new_node.value < temp.value  :
                    if temp.left is None :
                         temp.left = new_node
                         return True
                    temp = temp.left
               else :
                    if temp.right is None :
                         temp.right = new_node
                         return True
                    temp = temp.right

bst = BinarySearchTree()

bst.insert(2)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(6)







print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.right.value)




          

