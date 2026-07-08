
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
        current = self.head

        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")  # for newline after printing the list)

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current is not None and count < position - 1:
                current = current.next
                count += 1
                
            if current is None:
                print("Position out of bounds")
                return
                
            new_node.next = current.next
            current.next = new_node

sll = SinglyLinkedList()
sll.append(45)
sll.append(98)
sll.traverse()  # Output: 45 -> 98 -> None