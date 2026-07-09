

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head):
        pre = None
        current = head

        while current is not None:
            first = current.next
            current.next = pre
            pre = current
            current = first
        head = pre 
        return head   

    def printList(self, head):
        current = head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)   


solution = Solution()
print("Original liked list:")
solution.printList(head)

reversedhead = solution.reverseList(head)

print("Reversed linked list:")
solution.printList(reversedhead)

