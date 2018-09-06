class Queue:
    """docstring for queue."""
    def __init__(self):
        self.queue = list()

    def add(self, data):
        self.queue.insert(0, data)

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ('Queue is empty!')

    def peek(self):
        return self.queue[-1]

    def size(self):
        return self.queue


q = Queue()
print(q.remove())
print(q.add(1))
print(q.add(4))
print(q.size())
print(q.add(323))
print(q.size())
print(q.remove())
print(q.size())
