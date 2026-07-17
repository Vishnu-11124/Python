class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class List:
    def reverseList(self, head):
        if head.next is None:
            return head
        
        current = head
        prev = None
        
        while current is not None:
            temp = current.next
            current.next = prev
            current.prev = temp
            prev = current
            current = temp
        return prev 
        
    def printList(self, head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None") 

# ------------------------------------------------------------------
     
# Create nodes
head = Node(5)
second = Node(3)
third = Node(2)
fourth = Node(1)
fifth = Node(9)

# Connect next pointers
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Connect previous pointers
second.prev = head
third.prev = second
fourth.prev = third
fifth.prev = fourth

list = List()
print("Original list:")
list.printList(head)
new_head = list.reverseList(head)
print("Reversed list:")
list.printList(new_head)