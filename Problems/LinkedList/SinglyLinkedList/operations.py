
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): 
        new_node = Node(data) 
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node                   

    def traverse(self):
        curr = self.head
        if curr is None:
            print("List is empty")
        else:
            while curr is not None:
                print(curr.data, end=" ")
                curr = curr.next
            print()  # for newline after printing the list    


sll = SinglyLinkedList()
sll.append(45)
sll.append(98)
sll.traverse()  # Output: 45 98 