class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def calc_height(self, node):
        if node is None:
            return 0
        hLeft = self.calc_height(node.left)
        hRight = self.calc_height(node.right)
        if (hLeft > hRight):
            return hLeft+1
        else:
            return hRight+1

    def isbalanced(self, root):
        if root is None:
            return True

        lefthigh = self.calc_height(root.left)
        righthigh = self.calc_height(root.right)

        if ((lefthigh-righthigh) <= 1 and (righthigh-lefthigh) >= -1 and self.isbalanced(root.right) and self.isbalanced(root.left)):
            return True

        return False


d = TNode("D", None, None)
e = TNode("E", None, None)
b = TNode("B", d, e)
f = TNode("F", None, None)
c = TNode("C", f, None)
root = TNode("A", b, c)

print(root.isbalanced(root))
