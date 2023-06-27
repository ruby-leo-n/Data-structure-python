from code5 import CircularQueue

MAX_QSIZE = 4


class FiboCircularQueue(CircularQueue):
    def __init__(self):
        super().__init__()
        self.items = [0]*MAX_QSIZE

    def Fiboque(self, num):  # 피보나치 수열의 n번째 항의 값을 반환하는 함수
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:  # 삽입 후 삭제 & 이전 두 개의 원소의 합을 새롭게 삽입함
            self.enqueue(0)
            self.enqueue(1)
            for i in range(num-2):  # 피보나치 수열의 n번째 항의 값을 반환하기에 이전 두개는 횟수로 돌리지 않음
                self.enqueue(self.items[(self.front + 1) % MAX_QSIZE]
                             + self.items[(self.rear) % MAX_QSIZE])
                # front는 앞의 값을 가져오기때문에, rear는 바로 그 값을 가져오기 때문에
                self.dequeue()  # 포화상태 방지 & front의 위치 변경
            return self.items[self.rear]

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]


fiboque = FiboCircularQueue()

print(fiboque.Fiboque(90))
