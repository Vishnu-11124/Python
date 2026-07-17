class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtHead(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def appendNode(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp     

    def insertAtAnyPosition(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insertNodeAtHead(val)
            return

        current = self.head
        count = 0
        
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current    

    def deleteHead(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        self.head = temp.next

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")          

ddl = DoublyLinkedList()
ddl.insertNodeAtHead(26)
ddl.appendNode(87)
ddl.insertAtAnyPosition(17, 1)
ddl.deleteHead()
ddl.printList()


