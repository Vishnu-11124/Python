class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class List:
    def printPairs(self, head, target):
        left = head
        right = head
        result = []

        while right.next is not None:
            right = right.next

        while left is not None and right is not None and left.val < right.val:
            total = left.val + right.val
            if total > target:
                right = right.prev
            elif total < target:
                left = left.next
            else:
                result.append([left.val, right.val])  
                left = left.next
                right = right.prev

        return result                   

    def printList(self, head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None") 

# ------------------------------------------------------------------

n1 = Node(2)
n2 = Node(4)
n3 = Node(6)
n4 = Node(8)
n5 = Node(10)
n6 = Node(12)

# Next connections
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

# Previous connections
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4
n6.prev = n5

head = n1          

list = List()
print("Original List:")
list.printList(head)
pairs = list.printPairs(head, 10)
print("The pairs: ", pairs)
