import queue


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None

    def calc_height(self, node):
        if node is None:
            return 0
        hleft = self.calc_height(node.left)
        hright = self.calc_height(node.right)
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1

    def calc_height_diff(self, node):
        left = self.calc_height(node.left)
        right = self.calc_height(node.right)
        return left - right

    def rotateLL(self, A):
        B = A.left
        A.left = B.right
        B.right = A
        return B

    def rotateRR(self, A):
        B = A.right
        A.right = B.left
        B.left = A
        return B

    def rotateRL(self, A):
        B = A.right
        A.right = self.rotateLL(B)
        return self.rotateRR(A)

    def rotateLR(self, A):
        B = A.left
        A.left = self.rotateRR(B)
        return self.rotateLL(A)

    def reBalance(self, parent):
        diff = self.calc_height_diff(parent)

        if diff > 1:
            if self.calc_height_diff(parent.left) > 0:
                parent = self.rotateLL(parent)
            else:
                parent = self.rotateLR(parent)
        elif diff < -1:
            if self.calc_height_diff(parent.right) < 0:
                parent = self.rotateRR(parent)
            else:
                parent = self.rotateRL(parent)
        return parent

    def insert_avl(self, parent, node):
        if node.key < parent.key:
            if parent.left != None:
                parent.left = self.insert_avl(parent.left, node)
            else:
                parent.left = node
            return self.reBalance(parent)
        elif node.key > parent.key:
            if parent.right != None:
                parent.right = self.insert_avl(parent.right, node)
            else:
                parent.right = node
            return self.reBalance(parent)
        else:
            print("key Error")

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def insert(self, key, value=None):
        node = Node(key, value)
        if self.root == None:
            self.root = node
        else:
            self.root = self.insert_avl(self.root, node)

    def levelorder(self, root):
        self.queue = queue.Queue()
        self.queue.put(root)
        while not (self.queue.qsize() == 0):
            node = self.queue.get()
            if node is not None:
                print(node.key, end=" ")
                self.queue.put(node.left)
                self.queue.put(node.right)

    def display(self, msg="AVL tree:"):
        print(msg, end=" ")
        self.levelorder(self.root)
        print()


def main():
    avl = AVL()
    data = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    for key in data:
        avl.insert(key)
        avl.display()


if __name__ == '__main__':
    main()
