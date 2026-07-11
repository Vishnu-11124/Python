
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1 
                return count + 1   
        return None

# ----------------------------------------------------------- 

head = ListNode(5)
head.next = ListNode(9)
head.next.next = ListNode(1)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = head.next.next

sol = Solution()
print(sol.hasCycle(head))

# ----------------------------------------------------------- 

head = ListNode(5)
head.next = ListNode(9)
head.next.next = ListNode(1)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = None

sol = Solution()
print(sol.hasCycle(head))

# ----------------------------------------------------------- 

