# Prim 알고리즘:
# 하나의 정점에서 시작하여 현재까지 연결된 정점들에서 연결되지 않은 정점들에 대해,
# 가장 가중치가 작은 정점을 연결하는 정점 선택 기반으로 동작한다


INF = 999  # 가중치 중에서 가장 큰 수 (무한대)
#import sys
#INF = sys.maxsize


def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):  # 반복!
        if not selected[v] and dist[v] < mindist:  # 선택이 안되어 있는 것들 중 최소 가중치보다 적으면
            mindist = dist[v]  # 최소 가중치로 두고
            minv = v  # 최소 가중치의 정점을 저장
    return minv  # 반복 종료 후 최소 가중치의 정점을 반환
# selected는 MST에 선택된 정점인지 확인하는 역할
# dist는 MST에서 각각의 정점들로 향할 수 있는 간선들의 가중치를 저장하는 역할

# 각각의 정점들로 향할 수 있는 것들(선택되지 않은 것) 중에 가장 가중치가 적은 것을 선택하기 때문에
# 이미 선택된 정점이면 연결할 수 있는 간선이 있더라도 연결하지 않는다.
# 따라서 사이클이 만들어 지지 않는다.


def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = vsize*[INF]
    selected = [False] * vsize
    dist[0] = 0  # A부터 시작하겠다.

    for i in range(vsize):
        u = getMinVertex(dist, selected)  # 여기서 가장 작은 가중치의 정점을 찾음
        selected[u] = True  # 선택 됨
        print(vertex[u], end=" ")  # MST트리에 선택되었으므로 출력
        for v in range(vsize):
            if (adj[u][v] != None):  # 선택된 정점의 간선들의 탐색 만약 간선이 있으면
                # 아직 선택되지 않은 것들 중 dist에 적힌 값보다 작은 가중치를 가지면
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]  # 갱신 시킨다.
    print()


def main():
    vertex = ["A", "B", "C", "D", "E", "F", "G"]
    weight = [[None, 29, None, None, None, 10, None],
              [29, None, 16, None, None, None, 15],
              [None, 16, None, 12, None, None, None],
              [None, None, 12, None, 22, None, 18],
              [None, None, None, 22, None, 27, 25],
              [10, None, None, None, 27, None, None],
              [None, 15, None, 18, 25, None, None]]
    print("MST By Prim's Algorithm")
    MSTPrim(vertex, weight)


if __name__ == '__main__':
    main()

# Prim 알고리즘" 반복문이 정점의 수 n만큼 반복하고 내부 반복문이 n만큼 반복하므로 O(n^2)의 시간복잡도를 가진다.
# 따라서 완전 그래프와 같이 간선이 매우 많은 그래프의 경우 유리하다.

# 반대로 Kruskal 알고리즘은 O(eloge)의 시간 복잡도를 가지므로 정점의 개수에 비해 간선의 개수가 적은 희소 그래프의 경우 유리하다
