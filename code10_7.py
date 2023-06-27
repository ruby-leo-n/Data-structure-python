# 신장트리: 그래프 내의 모든 정점을 모함하는 트리이다.
# 신장트리도 트리의 일종이므로
# 1.모든 정점들이 연결되어 있어야 한다.
# 2.사이클이 없어야 한다.
# 3.그래프의 n개의 정점을 정확히 n-1개의 간선으로 연결해야 한다.
# 신장트리를 갖기 위해서는 깊이우선탐색이나 너비우선탐색을 사용할 수 있다.
# 신장트리는 깊이우선탐색이나 너비우선탐색 도중에 사용된 간선들을 모으면 된다.


import collections as cols


def bfsST(graph, start):  # 너비우선탐색을 수정해 탐색 도중에 추가되는 간선을 순서대로 출력한 코드
    visited = set([start])
    queue = cols.deque([start])
    while queue:
        v = queue.popleft()  # v는 큐에서 빼낸 원소
        nbr = graph[v] - visited
        for u in nbr:  # u = {v의 인접정점} - {방문정점}
            print("(", v, ",", u, ")", end=" ")  # 간선 추가
            visited.add(u)
            queue.append(u)


def main():
    Mygraph = {"A": {"B", "C"},
               "B": {"A", "D"},
               "C": {"A", "D", "E"},
               "D": {"B", "C", "F"},
               "E": {"C", "G", "H"},
               "F": {"D"},
               "G": {"E", "H"},
               "H": {"E", "G"}}
    bfsST(Mygraph, "A")


if __name__ == '__main__':
    main()
