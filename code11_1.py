# 인접 리스트를 이용한 표현
# 가중치 그래프를 인접리스트로 표현하는 것은 약간 더 복잡하다.
# 각 정점의 인접리스트에 정점만이 아니라 가중치를 추가로 저장해야 하기 때문이다.
# 정점과 가중치는 (정점,가중치)의 형태로 튜플로 표현하는 것이 좋다.

graphA = {"A": {("B", 29), ("F", 10)},
          "B": {("A", 29), ("C", 16), ("G", 15)},
          "C": {("B", 16), ("D", 12)},
          "D": {("C", 12), ("E", 22), ("G", 18)},
          "E": {("D", 22), ("F", 27), ("G", 25)},
          "F": {("A", 10), ("E", 27)},
          "G": {("B", 15), ("D", 18), ("E", 25)}
          }

# 인접 리스트에서의 가중치의 합 계산과 간선 출력
# 인접 리스트로 표현된 무방향 그래프에서도 간선들이 중복되어 나타나므로, 전체 결과를 2로 나누어야 실제 가중치 합이 된다.


def weightSum(graph):
    sum = 0
    for v in graph:
        for e in graph[v]:
            sum += e[1]
    return sum//2


def printAllEdges(graph):
    for v in graph:
        for e in graph[v]:
            print("(%s,%s,%d)" % (v, e[0], e[1]), end=" ")


def main():
    print("weightSum:", weightSum(graphA))
    printAllEdges(graphA)


if __name__ == '__main__':
    main()
