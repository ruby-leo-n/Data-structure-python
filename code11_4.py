# 최단경로 문제는 가중치 그래프에서 두 정점을 연결하는 여러 경로들 중에서 간선들의 가중치 합이 최소가 되는 경로를 찾는 문제이다.
# 또한, 간선의 가중치를 시간으로 하느냐, 거리로 하느냐에 따라 최단"시간" 경로나 최단"거리"경로를 선택해서 확인할 수 있다.
# 그래프의 정점은 각 도시가 될 것이고, 간선의 가중치는 도시간의 이동거리가 될 것이다.
# 두 정점 사이에 간선이 없으면 그 요소는 무한대의 값을 갖도록 한다. 또한 대각선 성분은 모두 0으로 처리하는데, 같은 도시에서는 이동거리가 0이기 때문이다.

# 어떤 방법으로 가중치 그래프에서 정점들 사이의 최단 경로를 구할 수 있을까?
# 다익스트라 알고리즘과 플로이드 알고리즘이 있다.
# 다익스트라 알고리즘은 하나의 시작 정점에서 다른 모든 정점까지의 최단 경로를 구한다.
# 이에 비해 플로이드 알고리즘은 모든 정점에서 다른 정점까지의 최단 경로를 한꺼번에 구할 수 있는 방법이다.

# 인접행렬에서 두 정점 사이의 간선이 없으면 None이 아니라 무한대 값(INF)을 저장한다.
# 인접행렬의 대각선 요소들은 모두 0으로 처리한다.
# 이때, 중요한 가정은 간선의 가중치는 반드시 양수라는 것이다. (가중치로 음수를 허용하지 않는다)


# 다익스트라 최단 경로 알고리즘은 하나의 시작 정점w에서 다른 모든 정점들까지의 최단 경로를 찾는 알고리즘이다.
# 모든 정점 u에 대해 시작 정점 v와의 간선 (u,v)가 없으면 dist[u]는 weight[v][u], 즉 간선(u,v)의 가중치로 초기화 된다.
# 만약 간선이 없으면 dist[u]는 무한대 값으로 초기화 된다.

# 기본 아이디어는 매 단계에서 S안에 있지 않은 정점들 중에서 가장 dist값이 작은 정점을 S에 추가하는 것이다.
# 정점이 추가되면 아직 S에 포함되지 못하고 남은 정점들의 dist를 갱신해야 한다.
# 이것은 새로운 정점이 S에 포함됨에 따라 자신과 S와의 거리가 더 가까워질 수 있기 때문이다.

# 만약 새로운 정점 u가 S에 추가되었다면 S에 있지 않은 다른 정점들의 dist값을 수정해야 한다.
# 새로 추가된 정점 u를 거쳐서 정점까지 가는 거리와 기존의 거리를 비교하여 더 작은 거리로 dist를 수정한다.
# 즉, 갱신되는 정점w는  dist[w] = min(dist[w] , dist[u] + dist[u][w])에 의해 갱신된다.


INF = 9999


def choose_vertex(dist, found):  # S안에 있지 않은 정점들 중에 dist값이 가장 적은 정점을 찾는 함수
    min = INF
    minpos = -1
    for i in range(len(dist)):
        if dist[i] < min and found[i] == False:
            min = dist[i]
            minpos = i
    return minpos

# vsize는 vtx의 길이
# dist는 시작 정점으로부터의 최단경로 거리를 저장
# found는 방문 정점 표시를 위해 사용, 최초 모든 항목이 False
# paht는 바로 이전 정점을 저장, 이전 정점을 따라 시장 정점까지 가는 경로가 최단 경로임


def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    path = [start]*vsize
    found = [False]*vsize
    found[start] = True
    dist[start] = 0

    for i in range(vsize):
        print("step_dist%2d " % (i+1), dist)  # 중간과정 출력
        print("step_path%2d " % (i+1), path)
        u = choose_vertex(dist, found)  # 최소 dist 정점 탐색
        print("step_u%5d " % (i+1), u, vtx[u])
        found[u] = True  # 방문한걸로 표시

        for w in range(vsize):  # 연결된 정점들의 최단거리 갱신
            if not found[w]:  # 방문하지 않은 것들 중에
                if dist[u] + adj[u][w] < dist[w]:  # 갱신 조건 검사
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u  # 이전 정점 갱신
                    # 갱신하면서 최소 경로를 새롭게 찾은 것은 선택된 최단 경로 정점을 포함한다는 뜻
    return path


def main():
    vertex = ["A", "B", "C", "D", "E", "F", "G"]
    weight = [[0, 7, INF, INF, 3, 10, INF],
              [7, 0, 4, 10, 2, 6, INF],
              [INF, 4, 0, 2, INF, INF, INF],
              [INF, 10, 2, 0, 11, 9, 4],
              [3, 2, INF, 11, 0, 13, 5],
              [10, 6, INF, 9, 13, 0, INF],
              [INF, INF, INF, 4, 5, INF, 0]]
    print("shortest Path by Dijkstra Algorithm:")
    start = 0
    path = shortest_path_dijkstra(vertex, weight, start)

    for end in range(len(vertex)):
        if end != start:
            print("[최단경로: %s->%s] %s" %
                  (vertex[start], vertex[end], vertex[end]), end=" ")
            while (path[end] != start):
                print("<- %s" % vertex[path[end]], end=" ")
                end = path[end]  # 키값을 인덱스로 보냄
            print("<- %s" % vertex[path[end]])


if __name__ == '__main__':
    main()
