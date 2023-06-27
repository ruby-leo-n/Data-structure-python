class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def reverse(self, root):
        if root == None:
            return False
        else:
            self.reverse(root.right)
            self.reverse(root.left)
            temp = root.right
            root.right = root.left
            root.left = temp
        return True

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


d = TNode("D", None, None)
e = TNode("E", None, None)
b = TNode("B", d, e)
f = TNode("F", None, None)
c = TNode("C", f, None)
root = TNode("A", b, c)

root.preorder(root)
print()
root.reverse(root)
root.preorder(root)
