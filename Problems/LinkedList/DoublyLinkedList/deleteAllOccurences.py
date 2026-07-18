class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class List:
    def deleteValues(self, head, key):
        if head is None:
            print("The list is empty")
            return 
        
        current = head
        pre = None
        while current is not None:
            if current.val == key:
                next = current.next
                pre.next = next
                next.prev = pre
                current = next
            else:
                next = current.next
                pre = current
                current = next    

    def printList(self, head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")            

# ----------------------------------------------------------------- 

n1 = Node(5)
n2 = Node(2)
n3 = Node(3)
n4 = Node(2)
n5 = Node(10)

head = n1
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4  

ddl = List()
print("Original list: ")
ddl.printList(head)

ddl.deleteValues(head, 2)
print("Updated list:")
ddl.printList(head)