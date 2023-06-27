from code7_5 import Entry


class Node:
    def __init__(self, elem, link):
        self.data = elem
        self.link = link


class HashChainMap:
    def __init__(self, M):
        self.table = [None]*M
        self.M = M

    def hashFn(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.M

    def insert(self, key, value):
        idx = self.hashFn(key)
        # 아래와 같이 풀어서 기술하는 것도 가능
        self.table[idx] = Node(Entry(key, value), self.table[idx])
        # entry = Entry(key,value) 1.엔트리 생성
        # node  = Node(entry) 2.엔트리로 노드를 생성
        # node.link = self.table[idx] 3.노드의 링크필드 처리
        # self.table[idx] = node 4.테이블의 idx항목: node로 시작

    def delete(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]
        before = None
        while node is not None:
            if node.data.key == key:
                if before == None:  # 첫번째 항목 삭제
                    self.table[idx] = node.link
                else:
                    before.link = node.link
                return
            before = node
            node = node.link

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] -> " % idx, end="")
                while (node is not None):
                    print(node.data, end="->")
                    node = node.link
                print()

    def search(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node = node.link
        return None


map2 = HashChainMap(5)
map2.insert("data", "자료")
map2.insert("structure", "구조")
map2.insert("sequential search", "선형탐색")
map2.insert("game", "게임")
map2.insert("binary search", "이진 탐색")
map2.display("나의 단어장:")

print("탐색: game ->", map2.search("game"))
print("탐색: data ->", map2.search("data"))
print("탐색: over ->", map2.search("over"))

map2.delete("game")
map2.display("나의 단어장:")
