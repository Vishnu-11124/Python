# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

# ----------------------------------------------------------------

# -------- Create Linked List --------
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# -------- Call Solution --------
sol = Solution()
middle = sol.middleNode(head)

print(middle.val)

# ----------------------------------------------------------------

# -------- Create Linked List --------
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
# -------- Call Solution --------
sol = Solution()
middle = sol.middleNode(head)

print(middle.val)

# ----------------------------------------------------------------
