from code7_4 import sequential_search
# 리스트를 이용한 순차탐색 맵


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s" % (self.key, self.value))


class SequentialMap:
    def __init__(self):
        self.table = []

    def size(self):
        return len(self.table)

    def display(self, msg):
        print(msg)
        for entry in self.table:
            print(" ", entry)

    def insert(self, key, value):
        self.table.append(Entry(key, value))

    def search(self, key):
        pos = sequential_search(self.table, key, 0, self.size()-1)
        if pos is not None:
            return self.table[pos]
        else:
            return None

    def delete(self, key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return


# map = SequentialMap()
# map.insert("data", "자료")
# map.insert("structure", "구조")
# map.insert("sequential search", "선형탐색")
# map.insert("game", "게임")
# map.insert("binary search", "이진 탐색")
# map.display("나의 단어장:")

# print("탐색: game ->", map.search("game"))
# print("탐색: data ->", map.search("data"))
# print("탐색: over ->", map.search("over"))

# map.delete("game")
# map.display("나의 단어장:")
