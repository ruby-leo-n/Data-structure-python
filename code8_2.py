class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self): return len(self.heap)-1

    def isEmpty(self): return self.size() == 0

    def Parent(self, i): return self.heap[i//2]

    def Left(self, i): return self.heap[i*2]

    def Right(self, i): return self.heap[i*2+1]

    def display(self, msg="힙 트리:"):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n > self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child < self.size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot
        # parent 변수는 부모를 그때그때 계산에서 부모를 가리키고
        # child 변수는 부모와 비교하는 자식,(즉, 부모의 자식 중 더 큰 자식을 가리킴 기본값: 왼쪽)
        # 만약 왼쪽보다 오른쪽 값이 더 큰 경우 child 값에 1을 더해서 오른쪽 값을 가리키게 함
        # parent변수와 마찬가지로 child변수도 그때그때 계산에서 가리키는 게 달라짐
        # last 변수는 힙트리에서 제일 마지막에 있는 값
        # last 변수가 child 변수보다 큰 경우, 그때의 parent변수에 last를 삽입한다. (마지막 줄에서 위로 두 줄 참고)
        # 그렇지 않은 경우 child 값을 부모가 있던 위치로 올리고 부모를 가리키는 변수 parent는 내려가서 자식을 가리킨다.
        # last와  hroot를 적절히 삭제 연산에 맞게 처리해준다. (마지막 줄에서 바로 윗줄까지의 case)


# heap = MaxHeap()
# data = [2, 5, 4, 8, 9, 3, 7, 3]
# print("삽입연산:", data)
# for elem in data:
#     heap.insert(elem)
#     heap.display("과정:")
# heap.display("삽입 후:")
# heap.delete()
# heap.display("삭제 후:")
# heap.delete()
# heap.display("삭제 후:")
