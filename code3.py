class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        self.items.pop(pos)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def getEntry(self, pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

    def clear(self):
        while not (self.isEmpty()):
            del self.items[0]

    def find(self, item):
        if self.isEmpty():
            return False
        elif self.isEmpty:
            if (item in self.items) == True:
                return self.items.index(item)
            else:
                return print("sorry")

    def replace(self, pos, item):
        self.items[pos] = item

    def sort(self, rev=0):
        if rev == 0:
            self.items.sort()
        elif rev == 1:
            self.items.sort(reverse=True)

    def merge(self, lst):
        self.items.extend(lst)

    def display(self):
        print(self.items)

    def append(self, e):
        self.items.append(e)


# listclass = ArrayList()

# print(listclass.isEmpty())

# listclass.insert(0, 10)
# listclass.insert(0, 100)
# listclass.insert(1, 110)
# listclass.insert(2, 510)
# listclass.insert(4, 109)
# listclass.insert(5, 60)
# listclass.insert(7, 102)
# listclass.display()

# listclass.append(70)
# listclass.append(80)
# listclass.display()

# listclass.sort(1)
# listclass.display()

# listclass.delete(3)
# listclass.display()

# listclass.replace(3, 50)
# listclass.display()

# print(listclass.isEmpty())

# print(listclass.find(60))

# listclass.clear()
# listclass.display()
