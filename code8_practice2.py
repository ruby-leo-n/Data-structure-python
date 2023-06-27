

class TNode_P:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.count = 0

    def level(self, root, node, lev=1):
        if root == None:  # root값이 None이면 재귀문에서 나옴
            return
        if root == node:  # 값을 찾으면 반환
            return lev
        if (root.left == None and root.right == None):
            return   # 양쪽 자식이 모두 없는 경우도 재귀문에서 나온다
        left = self.level(root.left, node, lev+1)  # return 값 lev을 저장
        right = self.level(root.right, node, lev+1)  # return 값 lev을 저장

        if (not left):  # 왼쪽 노드가 존재하지 않는다면
            return right  # 오른쪽 반환
        else:
            return left


d = TNode_P("D", None, None)
e = TNode_P("E", None, None)
b = TNode_P("B", d, e)
f = TNode_P("F", None, None)
c = TNode_P("C", None, f)
root = TNode_P("A", b, c)
print(root.level(root, f))
