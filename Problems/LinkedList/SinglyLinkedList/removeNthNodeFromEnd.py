class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class  Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head 

        for _ in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head        

    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

# ---------------------------------------------------------

head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(7)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next.next = None

list = Solution()
print("Original List:")
list.printList(head)
print("List after removing 3rd node from the end:")
head = list.removeNthFromEnd(head, 3)
list.printList(head)