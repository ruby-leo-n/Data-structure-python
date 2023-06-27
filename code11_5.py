# 만약 그래프의 모든 정점들 사이의 최단 경로를 구하려고 한다면 다익스트라 알고리즘을 정점의 수만큼 반복하여 실행하면 된다.
# 플로이드 알고리즘은 3중 반복을 하는 루프로 구성되어있어 그래프의 모든 정점 사이의 최단 경로를 한꺼번에 찾아준다.

# A^k[i][j]를 0부터 k까지의 정점만을 이용한 정점 i에서 j까지의 최단 경로라고 하자
# 우리가 구하려는 것은 0부터 n-1까지의 모든 정점을 이용한 최단 경로이기때문에 A^n-1[i][j]를 구하려고 한다.

# A^k-1까지는 완벽한 최단 거리가 구해져 있다고 가정하고, 이제 k번째 정점이 추가로 고려되는 상황이다.
# k번째 정점을 포함하여 0~k의 정점들을 사용하여 i에서 j로 가는 최단 경로는 다음의 2가지가 있다.
# 1. 정점 k를 거치지 않는 경로: A^k[i][j] <- A^k-1[i][j]
# 2. 정점 k를 통과하는 경로: A^k[i][j] <- A^k-1[i][k] + A^k-1[k][j]

# 1번은 지금까지 알고 있던 최적 경로이고, 2번은 i에서 k를 거쳐서 j로 오는 새로운 방법이다.
# k번째 정점을 포함하면 최단 경로는 이 경로들 중에 더 짧은 경로가 될 것이다.
# A^k[i][j] <- MIN(A^k-1[i][j], A^k-1[i][k] + A^k-1[k][j])

# 이것은 정점 k를 경유하는 것이 더 좋은 경로이면 값이 변경되고 아니면 이전의 값을 유지한다는 의미이다.


import copy
INF = 9999


def printA(A):
    vsize = len(A)
    print("============================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print(" INF", end=" ")
            else:
                print("%4d" % A[i][j], end=" ")
        print()


def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    # A = list(adj)
    # for i in range(vsize):
    #     A[i] = list(adj[i])
    # 객체 복사에 유의해야 한다. A = B는 새로운 리스트 객체를 만드는 것이 아니라 B가 가르키는 리스트를 변수 A가 참조한는 것
    # B가 가리키는 리스트와 동일한 새로운 리스트 객체를 만들고 이를 가리키도록 하려면 A = list(B) 처럼 처리한다.
    # 즉, 생성자를 이용해 새로운 객체를 생성하고 다음 변수 A가 이를 참조하도록 하는 것
    # 이차원 배열의 경우 A = list(adj)처럼 처리하면 새로운 리스트 객체는 생성되었지만
    # 리스트 안에 들어가는 리스트 객체들은 생성되지 않았기 때문이다. 즉, 위의 코드와 같이 각 행에 대한 리스트를 각각 생성하여 복사해야 한다.

    A = copy.deepcopy(adj)
    # copy모듈을 통해서 깊은 복사를 하면 이차원 배열도 쉽게 복사 가능

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if (A[i][k]+A[k][j] < A[i][j]):
                    A[i][j] = A[i][k]+A[k][j]
        printA(A)


def main():
    vertex = ["A", "B", "C", "D", "E", "F", "G"]
    weight = [[0, 7, INF, INF, 3, 10, INF],
              [7, 0, 4, 10, 2, 6, INF],
              [INF, 4, 0, 2, INF, INF, INF],
              [INF, 10, 2, 0, 11, 9, 4],
              [3, 2, INF, 11, 0, 13, 5],
              [10, 6, INF, 9, 13, 0, INF],
              [INF, INF, INF, 4, 5, INF, 0]]
    print("shortest Path by floyd Algorithm:")

    shortest_path_floyd(vertex, weight)


if __name__ == "__main__":
    main()

# 다익스트라 알고리즘을 정점 갯수 n만큼 반복하면 플로이드 알고리즘과 같은 값이 나온다.
# 위와 같은 다익스트라 알고리즘은 시간 복잡도가 O(n^3)이고 이것은 플로이드 알고리즘과 동일하다.
# 시간 복잡도 측면에서 차이는 없지만 플로이드 알고리즘은 매우 간결한 반복구문을 사용한다는 것이 특징이다.
