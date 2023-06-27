import queue


class TNode_P:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.list = []

    def levelorder(self, root):
        self.queue = queue.Queue()
        self.queue.put(root)
        while not (self.queue.qsize() == 0):
            node = self.queue.get()
            if node is not None:
                self.list.append(node.data)
                if node.left or node.right is not None:
                    self.queue.put(node.left)
                    self.queue.put(node.right)
            else:
                self.list.append(None)
        return self.list

    def is_complete_binary_tree(self, root):
        self.list = self.levelorder(root)
        if self.list[-1] == None:
            del self.list[-1]
        size = len(self.list)
        for i in range(0, size):
            if self.list[i] == None:
                return False
        return True


d = TNode_P("D", None, None)
e = TNode_P("E", None, None)
b = TNode_P("B", d, e)
f = TNode_P("F", None, None)
c = TNode_P("C", None, f)
root = TNode_P("A", b, c)

print(root.is_complete_binary_tree(root))
