# 파이썬을 이용한 그래프의 인접 리스트 표현
# 리스트와 튜플, 딕셔너리, 집합 등 인접 리스트를 표현할 수 있는 방법은 매우 다양하다.

# 하나의 객체로 표현
# 정점과 인접 리스트를 한꺼번에 표현할 수 있다.
# 여러 방법이 있지만 가장 간단한 방법은 정점과 그 정점의 리스트를 튜플(리스트)로 묶어 다음과 같이 하나로 처리하는 것이다.

graph = [("A", ["B", "C"]),
         ("B", ["A", "D"]),
         ("C", ["A", "D", "E"]),
         ("D", ["B", "C", "F"]),
         ("E", ["C", "G", "H"]),
         ("F", ["D"]),
         ("G", ["E", "F"]),
         ("H", ["E", "G"])]
# 변경이 필요가 없는 경우 리스트보다 튜플을 사용하는 것이 더 효율적이다.
# 이 방법으로 정점 C의 데이터와 객체에 접근하는 경우 graph[2][0]은 정점 C 객체이고 graph[2][1]은 정점 C의 인접 리스트이다.
# 정점 C의 첫번째 인접 정점은 graph[2][1][0]을 통해 알 수 있다.
# 실제 코드에서는 복잡함을 없애기 위해 다음과 같이 추가저긴 변수를 사용한다.

edge = graph[2][1]  # edge는 정점 C의 인접 리스트
print(edge[0])  # C의 첫번째 인접정점 출력