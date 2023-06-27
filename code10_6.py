# 연결성분 검사
# 연결 성분을 찾기 위해서 깊이우선탐색이나 너비우선탐색을 이용할 수 있다.
# 먼저 그래프의 임의의 정점을 선택하고 깊이우선탐색을 통해 연결되어 있는 모든 정점들을 출력한다
# 더 이상 연결된 정점이 없으면 그래프에서 아직 방문되지 않은 다른 정점을 선택해 동일한 과정을 되풀이한다.
# 이 과정을 그래프의 모든 정점이 방문될 때까지 반복하면 모든 연결 성분들을 찾을 수 있다.

def find_connected_component(graph):
    visited = set()  # 방문한 노드를 저장함
    colorList = []  # 연결된 그래프를 저장함

    for vtx in graph:  # 그래프의 모든 정점들에 대해
        if vtx not in visited:  # 방문하지 않은 정점이 있다면
            color = dfs_cc(graph, [], vtx, visited)  # 새로운 컬러 리스트
            colorList.append(color)  # 컬러 리스트에 컬러(list) 추가

    print("그래프 연결성분 갯수: %d" % len(colorList))
    print(colorList)


def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited:  # 아직 방문하지 않은 노드에 대해
        visited.add(vertex)  # 방문 마킹
        color.append(vertex)  # 컬러(list)에 원소 추가
        nbr = graph[vertex] - visited  # nbr: 차집합 연산 이용
        for v in nbr:
            dfs_cc(graph, color, v, visited)  # 재귀 호출
    return color  # 연결된 정점 리스트 반환


def main():
    Mygraph = {"A": {"B", "C"},
               "B": {"A"},
               "C": {"A"},
               "D": {"E"},
               "E": {"D"}}
    print("find_connected_component:")
    find_connected_component(Mygraph)


if __name__ == '__main__':
    main()
