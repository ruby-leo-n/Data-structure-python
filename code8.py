import queue


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def levelorder(self, root):
        self.queue = queue.Queue()
        self.queue.put(root)
        while not (self.queue.qsize() == 0):
            node = self.queue.get()
            if node is not None:
                print(node.data, end=" ")
                self.queue.put(node.left)
                self.queue.put(node.right)

    def count_node(self, node):
        if node is None:
            return 0
        else:
            return self.count_node(node.left) + self.count_node(node.right) + 1

    def count_leaf(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self.count_leaf(node.left) + self.count_leaf(node.right)

    def calc_height(self, node):
        if node is None:
            return 0
        hLeft = self.calc_height(node.left)
        hRight = self.calc_height(node.right)
        if (hLeft > hRight):
            return hLeft+1
        else:
            return hRight+1


# d = TNode("D", None, None)
# e = TNode("E", None, None)
# b = TNode("B", d, e)
# f = TNode("F", None, None)
# c = TNode("C", f, None)
# root = TNode("A", b, c)

# print("\n Inorder:\t", end="")
# root.inorder(root)
# print("\n Preorder:\t", end="")
# root.preorder(root)
# print("\n postorder:\t", end="")
# root.postorder(root)
# print("\n levelorder:\t", end="")
# root.levelorder(root)
# print()

# print("노드의 갯수: %d개" % (root.count_node(root)))
# print("단말의 갯수: %d개" % (root.count_leaf(root)))
# print("트리의 높이: %d" % (root.calc_height(root)))
