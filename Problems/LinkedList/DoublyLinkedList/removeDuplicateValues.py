class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class List:
    def removeDuplicates(self, head):
        current = head

        while current is not None and current.next is not None:

            if current.val == current.next.val:

                duplicate = current.next
                current.next = duplicate.next

                if duplicate.next is not None:
                    duplicate.next.prev = current

            else:
                current = current.next

        return head   

    def printList(self, head):
        temp = head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None") 

# ----------------------------------------------------------------

# Create nodes
n1 = Node(2)
n2 = Node(2)
n3 = Node(3)
n4 = Node(5)
n5 = Node(5)
n6 = Node(8)
n7 = Node(10)

# Next connections
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

# Previous connections
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4
n6.prev = n5
n7.prev = n6

# Head
head = n1

list = List()
print("Original list:")
list.printList(head)

list.removeDuplicates(head)
print("List after remove duplicates:")
list.printList(head)
