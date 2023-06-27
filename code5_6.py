import math
from code5_5 import priorityQueue

(ox, oy) = (5, 3)


def dist(x, y):
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)


map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]

MAZE_SIZE = 6

# x,y가 갈 수 있는 방인지 검사하는 함수


def isValipos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or x >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def findMaxIndex():
    q = priorityQueue()
    if q.isEmpty():
        return None
    else:
        highest = 0
        for i in range(1, q.size()):
            if q.items[i][2] > q.items[highest][2]:
                highest = i
        return highest


def MysmartSearch():
    q = priorityQueue()
    q.enqueue((0, 1, -dist(0, 1)))
    print("PQueue: ")

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end=" ")
        x, y, _ = here
        if (map[y][x] == "x"):
            return True
        else:
            map[y][x] = "."
            if isValipos(x, y-1):
                q.enqueue((x, y-1, -dist(x, y-1)))
            if isValipos(x, y+1):
                q.enqueue((x, y+1, -dist(x, y+1)))
            if isValipos(x-1, y):
                q.enqueue((x-1, y, -dist(x-1, y)))
            if isValipos(x+1, y):
                q.enqueue((x+1, y, -dist(x+1, y)))
        print("우선순위큐: ", q.items)
    return False


result = MysmartSearch()
if result:
    print("---> 미로 탐색 성공")
else:
    print("---> 미로 탐색 실패")
