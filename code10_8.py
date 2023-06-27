# 위상정렬: 방향 그래프에 존재하는 각 정점들의 선행순서를 위배하지 않으면서 모든 정점을 나열하는 것
# 위상정렬을 위해서는 방향 그래프에 사이클이 존재하지 않아야 한다.
# 싸이클이 존재한다는 것은 싸이클상의 모든 과목이 선수과목을 갖게 되기 때문에 어떤 교과목도 수강할 수 없음을 말한다.
# 따라서 싸이클이 존재하면 위상정렬을 사용할 수 없다.


# 방향그래프의 위상정렬 알고리즘
# 1.진입차수가 0인 정점을 선택하고 선택된 점점과 연결된 모든 간선을 삭제한다.
# 2.이때 간선이 삭제되므로 삭제되는 간선과 연결된 남아있는 정점들의 진입차수도 수정되어야 한다.
# 3.이 과정을 반복하여 모든 정점이 삭제되면 알고리즘을 종료한다.
# 전체과정에서 삭제되는 순서가 위상순서이다.
# 만약 진입차수가 0인 정점이 여러개 있다면 어느 정점을 선택해도 된다.
# 만약 그래프에 남아있는 정점들 중에 진입차수가 0인 정점이 없다면 위상정렬은 불가능하다.
# 이것은 그래프에 사이클이 존재하는 것을 말한다.

def topological_sort_AM(vertex, graph):
    n = len(vertex)  # 각 정점의 갯수 파악
    inDeg = [0]*n  # inDeg는 각 정점의 진입차수를 기록하는 list

    # 각 정점의 진입차수를 기록: 이중for문을 이용
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:  # 모든 원소를 순회
                inDeg[j] += 1  # 열에 있는 1의 갯수가 진입차수임

    vlist = []  # 진입차수가 0인 정점을 모음

    for i in range(n):
        if inDeg[i] == 0:  # inDeg리스트를 조사해서 진입차수가 0인
            vlist.append(i)  # vertex의 index를 저장

    while len(vlist) > 0:  # vlist가 공백이 될 때까지 반복한다.
        v = vlist.pop()  # vlist에서 index 하나를 꺼내온다.
        print(vertex[v], end=" ")  # vertex에서 index에 있는 값을 출력

        for u in range(n):
            if v != u and graph[v][u] > 0:
                # (1,1),(2,2)...등등 제외[자기자신은 포함 x], 행을 고정시키고 열을 계속 이동하면서 0보다 클 때
                inDeg[u] -= 1  # 1 감소시킴
                if inDeg[u] == 0:  # 만약 0이 된 경우 vlist에 추가
                    vlist.append(u)


def main():
    vertex = ["A", "B", "C", "D", "E", "F"]
    graphAM = [[0, 0, 1, 1, 0, 0],
               [0, 0, 0, 1, 1, 0],
               [0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0]]
    print("topological_sort:")
    topological_sort_AM(vertex, graphAM)
    print()


if __name__ == '__main__':
    main()
