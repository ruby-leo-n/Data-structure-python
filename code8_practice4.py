# 참조: https://stackoverflow.com/questions/12529420/recursive-definition-of-path-length-of-a-tree

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.count = 1

    def count_node(self, root):
        if root is None:
            return 0
        else:
            return 1+self.count_node(root.left) + self.count_node(root.right)

    def path_length(self, root, totalNodes):
        if (totalNodes == 1) or (totalNodes == 0):
            return 0
        noOfNodes1 = self.count_node(root.left)
        noOfNodes2 = self.count_node(root.right)
        return (self.path_length(root.left, noOfNodes1)
                + self.path_length(root.right, noOfNodes2) + totalNodes - 1)


d = TNode("D", None, None)
e = TNode("E", None, None)
b = TNode("B", d, e)
f = TNode("F", None, None)
c = TNode("C", f, None)
root = TNode("A", b, c)

print(root.path_length(root, root.count_node(root)))
