class Set:
    def __init__(self):
        self.items = []  # 고정해서 사용 즉, 클래스에서 유일하다

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)

    def contains01(self, item):
        return item in self.items

    # def contains02(self, item):
    #     for i in range(len(self.items)):
    #         if(self.items[i]==item):
    #             return True
    #     return False

    def insert(self, item):
        if item not in self.items:
            self.items.append(item)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):  # 합집합
        setC = Set()  # 구조만 넘겨 받았다.
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC

    def intersect(self, setB):  # 교집합
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC


# setA = Set()
# setA.insert("휴대폰")
# setA.insert("지갑")
# setA.insert("노트북")
# setA.insert("손수건")
# setA.insert("야구공")
# setA.display("setA:")

# setB = Set()
# setB.insert("폰")
# setB.insert("수갑")
# setB.insert("노트")
# setB.insert("수건")
# setB.insert("야구공")
# setB.display("setB:")

# setB.delete("폰")
# setA.delete("손수건")
# setA.delete("발수건")
# setA.display("setA after:")
# setB.display("setB after:")

# setA.contains01("야구공")
# setA.union(setB).display("합집합:")
# setA.intersect(setB).display("교집합:")
# setA.difference(setB).display("A차집합:")
# setB.difference(setA).display("B차집합:")
