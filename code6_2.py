from code6 import Node


class CircularLinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None

    def clear(self):
        self.tail = None

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

    def enqueue(self, item):  # 큐의 삽입은 후단에서 이루어진다.
        node = Node(item, None)
        if self.isEmpty():  # 1 큐가 공백상태일 때
            node.link = node
            self.tail = node
        else:  # 2 큐가 공백상태가 아닐 때
            node.link = self.tail.link  # 새로운 노드는 전단을 가리키고
            self.tail.link = node  # 후단노드는 새로운 노드를 가리키고
            self.tail = node  # tail은 새로운 노드를 가리킴

    def dequeue(self):  # 큐는 전단에서 삭제가 이루어진다.
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                node = self.tail.link
                self.tail.link = node.link
            return data

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while node != self.tail:
                count += 1
                node = node.link
            return count

    def display(self, msg="CircularLinkedQueue"):
        print(msg, end=" ")
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=" ")
                node = node.link
            print(node.data, end=" ")
        print()


# q = CircularLinkedQueue()

# for i in range(10):
#     q.enqueue(i)
# q.display()

# for i in range(4):
#     q.dequeue()
# q.display()

# print("peek:", q.peek(), " size:", q.size())

# q.clear()
# q.display()
