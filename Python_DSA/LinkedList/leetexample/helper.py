from sol import Solution, ListNode

# Helper function to create a linked list from a list of numbers
def create_linked_list(values):
    dummy = ListNode
    current = dummy
    for value in values:
        current.next = Solution.ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Input linked lists
l1 = create_linked_list([2, 4, 3])  # Represents 342
l2 = create_linked_list([5, 6, 4])  # Represents 465

# Solution
solution = Solution()
result = solution.addTwoNumbers(l1, l2)  # Result: 7 -> 0 -> 8 (807)

# Print the result
print("Result Linked List:")
print_linked_list(result)
