# 집합에서 정렬
# 삽입연산
from code3_2 import Set


class NewSet(Set):
    def __init__(self):
        super().__init__()

    def newinsert(self, elem):
        if elem in self.items:
            return
        for index in range(len(self.items)):
            if elem < self.items[index]:
                self.items.insert(index, elem)
                return
        self.items.append(elem)

    def __eq__(self, setB):
        if self.size() != setB.size():
            return False
        for idx in range(len(self.items)):
            if self.items[idx] != setB.items[idx]:
                return False
        return True

    def newunion(self, setB):
        newSet = Set()
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = self.items[b]

            if valueA < valueB:
                newSet.items.append(valueA)
                a += 1

            elif valueA > valueB:
                newSet.items.append(valueB)
                b += 1

            else:
                newSet.items.append(valueA)
                a += 1
                b += 1
        while (a < len(self.items)):
            newSet.items.append(self.items[a])
            a += 1
        while (a < len(setB.items)):
            newSet.items.append(setB.items[b])
            b += 1
        return newSet


setx = NewSet()
setx.newinsert(3)
setx.newinsert(2)
setx.newinsert(1)
setx.newinsert(5)
setx.newinsert(4)
setx.newinsert(6)
setx.newinsert(9)
setx.newinsert(8)

sety = NewSet()
sety.newinsert(8)
sety.newinsert(5)
sety.newinsert(2)
sety.newinsert(9)
sety.newinsert(1)
sety.newinsert(3)

print(setx.newunion(sety).items)
print(setx.__eq__(sety))
