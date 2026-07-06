
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



node1 = Node(2)
node2 = Node(6)
node3 = Node(8)
node4 = Node(23)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1.data)
print(node2.data)
print(node3.data)
print(node4.data)