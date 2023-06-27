class DNode:
    # def __init__(self, prev=None, next=None, elem):
    # #default가 non-default 앞에 와서 뜨는 에러인데,함수의 Parameter 문법상 non-default가 앞에 와야 한다
    def __init__(self, elem, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = elem


class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): return self.front == None

    def clear(self): self.front = self.rear = None

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.front
            while not node == self.rear:
                count += 1
                node = node.next
            return count

    def display(self, msg="DoublyLinkedDeque:"):
        print(msg, end=" ")
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end=" ")
                node = node.next
            print(node.data, end=" ")
        print()

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if self.isEmpty():
            self.rear = self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear == None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data


dq = DoublyLinkedDeque()

for i in range(5):
    dq.addFront(i)

dq.display()

for i in range(5, 10):
    dq.addRear(i)

dq.display()

for i in range(3):
    dq.deleteFront()

dq.display()

for i in range(2):
    dq.deleteRear()

dq.display()

print(dq.size())

dq.clear()
dq.display()
