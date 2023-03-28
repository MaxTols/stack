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


bracket_dict = dict()
bracket_dict['('], bracket_dict['['], bracket_dict['{'] = ')', ']', '}'


def balance(string):
    stack = Stack()
    for elem in string:
        if elem in [key for key, value in bracket_dict.items()]:
            stack.push(elem)
        elif elem in [value for key, value in bracket_dict.items()]:
            last_elem = stack.peek()
            if stack.is_empty():
                return False
            elif elem == bracket_dict[last_elem]:
                stack.pop()
            else:
                return False
        else:
            return False
    return stack.is_empty()


# print(balance('(((([{}]))))'))
# print(balance('[([])((([[[]]])))]{()}'))
# print(balance('{{[()]}}'))

# print(balance('}{}'))
# print(balance('{{[(])]}}'))
# print(balance('[[{())}]'))

print(balance(input('Enter string: ')))
