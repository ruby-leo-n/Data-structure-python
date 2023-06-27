# class Node:
#     def __init__(self, elem, link=None):
#         self.data = elem
#         self.link = link

from code6 import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None
    def clear(self): self.head = None

    def size(self):
        count = 0
        node = self.head
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedStack:"):
        print(msg, end=" ")
        node = self.head
        if node == None:
            print("None", end=" ")
        while not node == None:
            print(node.data, end=" -> ")
            node = node.link
            if node == None:
                print("None", end=" ")
        print()

    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos):  # 항목의 데이터만 반환
        node = self.getEntry(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None:
            node.data = elem

    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:  # 맨 앞에 삽입하는 경우
            self.head = Node(elem, self.head)
        else:  # 중간에 삽입하는 경우
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:  # 시작노드를 삭제하는 경우,시작노드의 이전이므로 None값이다.
            if self.head is not None:  # 공백이 아니면
                self.head = self.head.link
        elif before.link != None:  # 중간에 있는 노드를 삭제
            before.link = before.link.link  # before의 링크의 링크 2번 넘어감 따라서 pos 삭제


# s = LinkedList()

# s.display("단순연결리스트로 구현한 리스트(초기상태):")
# s.insert(0, 10)
# s.insert(0, 20)
# s.insert(1, 30)
# s.insert(s.size(), 40)
# print(s.getNode(s.size()-1))

# s.insert(2, 50)
# s.display("단순연결리스트로 구현한 리스트(삽입):")

# s.replace(2, 90)
# s.display("단순연결리스트로 구현한 리스트(교체):")

# s.delete(2)
# s.delete(s.size()-1)  # 마지막 요소 삭제
# s.delete(0)
# s.display("단순연결리스트로 구현한 리스트(삭제):")

# s.clear()
# s.display("단순연결리스트로 구현한 리스트(정리 후):")
