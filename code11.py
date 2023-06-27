# #가중치그래프: 간선에 비용이나 가중치가 할당된 그래프
# 가중치 그래프는 수학적으로 G = (V,E,w)로 표현한다.
# v(G)는 그래프 G의 정점들의 집합을, E(G)는 그래프 G의 간선들의 집합을 의미하고, w(e)는 간선 e의 강도로 비용이나 길이라고 부른다.

# 인접행렬에 가중치를 저장하는 것은 매우 간단하다.
# 행렬의 각 요소에 0이나 1이 아니라 가중치 값을 저장하면 되기 때문이다.
# 만약 간선이 없으면 가중치를 None으로 저장한다.
# 즉, None이 아닌 값을 가지면 간선이 존재하는 것이고 None이면 간선이 없는 것으로 생각할 수 있다.

# 인접행렬 표현에서 대각선 성분에 유의해야 한다.
# 대각선 성분은 어떤 정점에서 자신으로 돌아오는 자체 간선에 해당하는 요소이다.

vertex = ["A", "B", "C", "D", "E", "F", "G"]
weight = [[None, 29, None, None, None, 10, None],
          [29, None, 16, None, None, None, 15],
          [None, 16, None, 12, None, None, None],
          [None, None, 12, None, 22, None, 18],
          [None, None, None, 22, None, 27, 25],
          [10, None, None, None, 27, None, None],
          [None, 15, None, 18, 25, None, None]]
graph = (vertex, weight)  # 전체 그래프: 튜플 사용
# 위의 코드와 같이 정점 리스트와 인접 행렬을 튜플로 묶어 전체 그래프를 하나의 객체로 관리할 수 있다.


# 인접행렬에서의 가중치의 합 계산

def weightSum(vlist, W):
    sum = 0
    for i in range(len(vlist)):
        for j in range(i+1, len(vlist)):  # 삼각영역
            if W[i][j] != None:  # 간선이 있으면
                sum += W[i][j]  # sum에 더함
    return sum  # 가중치 합 반환


def printAllEdges(vlist, W):
    for i in range(len(vlist)):
        for j in range(i+1, len(W[i])):  # 삼각영역
            if W[i][j] != None and W[i][j] != 0:  # 0과 None이 아닌 경우
                print("(%s,%s,%d)" % (vlist[i], vlist[j], W[i][j]), end=" ")
    print()


def main():
    print("AM: weight sum = ", weightSum(vertex, weight))
    printAllEdges(vertex, weight)


if __name__ == '__main__':
    main()
