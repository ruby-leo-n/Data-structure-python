from code9 import *


class BSTMap():
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def count_node(self, node):
        if node is None:
            return 0
        else:
            return self.count_node(node.left) + self.count_node(node.right) + 1

    def isEmpty(self):
        return self.root == None

    def Clear(self):
        self.root = None

    def size(self):
        return self.count_node(self.root)

    def search(self, key):
        return search_bst_recusive(self.root, key)

    def searchValue(self, key):
        return search_bst_value(self.root, key)

    def findMax(self):
        return search_max_bst_recusive(self.root)

    def findmin(self):
        return search_min_bst(self.root)

    def insert(self, key, value=None):
        node = BSTNode(key, value)
        if self.isEmpty():
            self.root = node
        else:
            insert_bst(self.root, node)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg="BSTMap"):
        print(msg, end=" ")
        self.inorder(self.root)
        print()


def main():
    map = BSTMap()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    print("[삽입연산]:", data)
    for key in data:
        map.insert(key)
    map.display("[중위순회]:")
    if map.search(26) != None:
        print("[탐색 26]: 성공")
    else:
        print("[탐색 26]: 실패")
    if map.search(25) != None:
        print("[탐색 25]: 성공")
    else:
        print("[탐색 25]: 실패")

    map.delete(3)
    map.display("[    3 삭제]:")
    map.delete(68)
    map.display("[   68 삭제]:")
    map.delete(18)
    map.display("[   18 삭제]:")
    map.delete(35)
    map.display("[   35 삭제]:")


if __name__ == '__main__':
    main()
