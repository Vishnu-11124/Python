
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        
        odd = head
        even_head = head.next
        even = even_head
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
    
    def printList(self, head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


# -------------------------------------------------------------

head = Node(8)
head.next = Node(1)
head.next.next = Node(6)
head.next.next.next = Node(9)
head.next.next.next.next = Node(7)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next.next = None

sol = Solution()
print("Original List:")
sol.printList(head)
result = sol.oddEvenList(head)
print("Rearranged List:")
sol.printList(result)