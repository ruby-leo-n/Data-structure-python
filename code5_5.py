class priorityQueue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
        for i in range(1, self.size()):
            if self.items[i] > self.items[highest]:
                highest = i
        return highest

    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)

    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]


# q = priorityQueue()
# q.enqueue(34)
# q.enqueue(18)
# q.enqueue(3)
# q.enqueue(8)
# q.enqueue(10)
# q.enqueue(27)

# print("PQueue:", q.items)
# while not q.isEmpty():
#     print("Max priority = ", q.dequeue())

# 일반적으로 우선순위 큐는 힙이라는 트리구조로 구현되어야 함
# 삽입과 삭제가 모두 (logn)으로 동작함
