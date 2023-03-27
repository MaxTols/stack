class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        remove = self.stack.pop()
        return remove

    def peek(self):
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        return element

    def size(self):
        size = len(self.stack)
        return size


def balanced(s):
    stack = Stack()
    for c in s:
        if c in '([{':
            stack.push(c)
        elif c in '}])':
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()


print(balanced(input('Enter text: ')))
