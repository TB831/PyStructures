class Stack:
    """docstring for stack."""
    def __init__(self):
        self.stack = list()

    def add(self, data):
        self.stack.insert(0, data)

    def remove(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)
        return ('Stack is empty!')

    def peek(self):
        return self.stack[0]

    def size(self):
        return self.stack

s = Stack()
print(s.size())
print(s.add(1))
print(s.add('wweeee'))
print(s.size())
print(s.add('asdfja'))
print(s.peek())
print(s.remove())
print(s.size())
