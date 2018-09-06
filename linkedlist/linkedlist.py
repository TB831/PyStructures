class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertFirst(self, data):
        self.head = Node(data, self.head)

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next
        return counter

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node.data
            node = node.next
        return 'Node not found'

    def delete(self, data):
        node = self.head
        previous = None
        found = False

        while node and found is False:
            if node.data == data:
                found = True
            else:
                previous = node
                node = node.next
            if node is None:
                raise ValueError('Data not in list')
            if previous is None:
                self.head = node.next

list = LinkedList()
node = Node()

print(list.insertFirst(1))
print(list.size())
print(list.insertFirst(2))
print(list.insertFirst('weee'))
print(list.size())
print(list.search(3))
print(list.search(2))
print(list.search('weee'))
print(list.delete('weee'))
print(list.size())
