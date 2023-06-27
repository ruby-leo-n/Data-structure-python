# 가중치 그래프에서 가장 적은 비용으로 망을 구축하는 문제를 생각해보자
# 1.그래프의 모든 정점들은 연결되어야 한다.
# 2.연결에 필요한 간선의 가중치 합(비용)이 최소가 되어야 한다.
# 3.사이클은 두 정점을 연결하는 두가지 경로 제공하므로 비용 사이클을 없애려면 n-1개의 간선만을 사용해야 한다.

# 최소비용 신장 트리는 이와 같이 그래프의 여러 가능한 신장트리 중에서 사용된 간선들의 가중치 합이 최소인 신장 트리를 말한다.
# 최소비용 신장 트리를 구하는 방법에는 Kruskal과 Prim 알고리즘이 있다.

# Kruskal 알고리즘
# 탐욕적인 방법이라는 알고리즘 설계에서 중요한 기법 중의 하나를 사용한다.
# "그 순간에 최적"이라 생각되는 것을 선택하는 방법이다.
# 순간에 최적이라고 판단했던 선택을 모아 최종적인 답을 만들었을 때 궁극적으로 최적이라는 보장이 없다.
# 따라서 탐욕적인 방법은 항상 최적의 해답을 주는 지를 반드시 검증해야 한다.
# 다행히 Kruskal 알고리즘은 최적의 해답을 주는 것으로 증명되어 있다.

# 증명) 참조: https://stalker5217.netlify.app/algorithm/kruskal/
# 일반적인 Greedy algorithm을 정당성을 증명하는 방식으로 증명 가능하다.
# 최소 스패닝 트리를 T라고 하고, 크루스칼 알고리즘으로 구현했을 때 포함되는 간선이 최소 스패닝 트리 T에는 포함되어 있지 않다고 가정한다.
# 만약 크루스칼 알고리즘이 선택한 간선이 정점 u와 v를 연결한다고 하면, T는 해당 간선이 아닌 다른 어떠한 경로로 u와 v를 연결하고 있다.
# 이 경로에 포함된 간선 중 하나는 분명히 크루스칼이 선택한 이 간선의 가중치 보다 크다.
# 그렇지 않으면 해당 경로를 구성하는 간선들이 크루스칼 알고리즘에 의해 이전에 모두 선택되어 이미 u와 v를 연결하는 경로가 존재한다는 모순에 빠진다.
# 만약 지금 선택된 간선보다 큰 가중치를 가지는 놈을 제거하고 크루스칼이 현재 선택한 간선으로 대체를 한다해도
# T가 이미 최소 스패닝 트리이기 때문에 스패닝 트리임을 증명할 수 있다.


# kruskal 알고리즘에서 사이클이 생기는지 검사하는 방법도 해결해야 한다.
# # 이미 선택된 간선들의 집합에 새로운 간선을 추가할 때 사이클이 생기는지 검사해야 한다.
# # 양끝 정점이 서로 다른 집합에 속한 경우 사이클이 형성되지 않는다.
# 추가하고자 하는 간선의 양끝 정점이 서로 같은 집합에 속하는지 먼저 검사해야 한다.
# 이를 위해 union-find를 사용하는데 다른 알고리즘에서 널리 사용되는 방법이다.
# union-find는 서로소인 집합들을 표현할 때 사용하는 독특한 형태의 집합 자료구조이다.
# 참조: https://maetdori.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Kruskal-Algorithm-Union-Find-%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9C%A0%EB%8B%88%EC%98%A8-%ED%8C%8C%EC%9D%B8%EB%93%9C


parent = []  # 그래프의 모든 정점에 대해 부모노드의 인덱스를 저장하기 위해서
set_size = 0  # 현재 집합의 갯수


def init_set(nSets):  # 초기화 함수
    global set_size, parent  # 전역변수 변경을 위해
    set_size = nSets
    for i in range(nSets):
        # 부모가 -1인 노드는 모두 루트노드이다. & 초기화 함수에서는 모든 정점들이 각가 고유집합이 되도록 초기화한다.
        parent.append(-1)


def find(id):  # id가 속한 집합을 찾는 함수로, 실제로는 id가 속한 트리의 루트노드의 인덱스를 반환하는 함수
    while (parent[id] >= 0):  # 부모가 있는 동안 (-1이 아닌 동안)
        id = parent[id]  # id를 부모id로 갱신
    return id  # 같은 집합에 속하는 모든 정점은 모두 같은 인덱스를 반환한다.


def union(s1, s2):  # 두 집합이 합해지므로 전체 집합의 수 set_size는 줄어들어야 한다.
    global set_size  # 전역변수를 변경하기 위해 global로 선언해야 한다.
    parent[s1] = s2  # s1을 s2에 병합함
    set_size -= 1


# Kruskal 알고리즘 구현
# 초기에는 모든 정점이 각각 고유한 집합이다.
# 최소 가중치 간선이 선택되면 선택된 원소가 각각 속한 집합을 찾는다. 이때 find(v),find(u)연산을 수행한다.
# 두 집합이 같으면 사이클이 발생하는 상황이므로 이 간선을 버린다.
# 두 집합이 다르면 간선을 삽입하고 집합을 하나로 합친다. 이때 union(u,v)연산을 사용한다.

def MSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []  # 간선 리스트

    for i in range(vsize-1):
        for j in range(i+1, vsize):
            if adj[i][j] != None:
                eList.append((i, j, adj[i][j]))

    eList.sort(key=(lambda e: e[2]), reverse=True)
    # 정렬할 항목들이 튜플이고 이 중에서도 weight 순으로 정렬해야 함으로 람다함수를 사용한다.

    edgeAccepted = 0

    while (edgeAccepted < vsize-1):
        e = eList.pop(-1)
        uset = find(e[0])
        vset = find(e[1])
        # 다른 집합 원소인 경우 간선을 추가하기 때문에 union-find에서 부모 인덱스를 -1로 모두 초기화 해도 상관없다.
        if uset != vset:  # 두 정점이 서로 다른 집합의 원소이면
            print("간선 추가: (%s,%s: %d)" % (vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            edgeAccepted += 1


def main():
    vertex = ["A", "B", "C", "D", "E", "F", "G"]
    weight = [[None, 29, None, None, None, 10, None],
              [29, None, 16, None, None, None, 15],
              [None, 16, None, 12, None, None, None],
              [None, None, 12, None, 22, None, 18],
              [None, None, None, 22, None, 27, 25],
              [10, None, None, None, 27, None, None],
              [None, 15, None, 18, 25, None, None]]
    print("MST By Kruskal's Algorithm")
    MSTKruskal(vertex, weight)


if __name__ == '__main__':
    main()
