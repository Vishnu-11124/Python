class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class List:
    def deleteValues(self, head, key):
        if head.next is None and head.val == key:
            return None

        temp = head
        pre = None
        new_head = head

        while temp is not None:
            if temp.val == key:
                if pre is not None:
                    pre.next = temp.next

                if temp.next is not None:
                    temp.next.prev = pre    

                if new_head.val == key:
                    new_head = new_head.next    

            pre = temp
            temp = temp.next    

        return new_head    
                
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

new_head = ddl.deleteValues(head, 2)
print("Updated list:")
ddl.printList(new_head)