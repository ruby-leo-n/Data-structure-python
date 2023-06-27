class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self): return self.top == None

    def clear(self): self.top = None

    def push(self, item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def size(self):
        count = 0
        node = self.top
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedStack:"):
        print(msg, end=" ")
        node = self.top
        while not node == None:
            print(node.data, end=" ")
            node = node.link
        print()


# ls = LinkedStack()

# ls.push(95)
# ls.display()
# ls.push(3)
# ls.display()
# ls.push(68)
# ls.display()
# ls.push(92)
# ls.display()
# ls.push(24)
# ls.display()
# ls.push(84)
# ls.display()
# ls.push(17)
# ls.display()
# ls.push(63)
# ls.display()
# ls.push(42)
# ls.display()

# ls.display()
# print(ls.size())

# ls.pop()
# ls.pop()
# ls.pop()

# ls.display()
# print(ls.peek())

# ls.clear()
# ls.display()
