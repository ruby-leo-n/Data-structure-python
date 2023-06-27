import queue

Q = queue.Queue(maxsize=20)
S = queue.LifoQueue(maxsize=20)  # 스택 클래스도 큐 모듈에서 제공한다. 객체생성방법이나 연산들은 큐와 동일하다.

for v in range(0, 20):
    Q.put(v)

print("큐의 내용:", end='')

for i in range(0, 10):
    print(Q.get(), end=" ")
