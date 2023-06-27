class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def search_bst_recusive(node, key):  # 재귀적 표현
    if node == None:
        return None
    elif key == node.key:
        return node
    elif key < node.key:
        return search_bst_recusive(node.left, key)
    else:
        return search_bst_recusive(node.right, key)


def search_bst_iter(node, key):  # 반복적 표현
    while (node != None):
        if key == node.key:
            return node
        elif key < node.key:
            node = node.left
        else:
            node = node.right
    return None


def search_bst_value(node, value):  # key로 탐색하는게 아닌 value값으로 탐색, 모든 노드를 순회함
    if node == None:
        return None
    elif value == node.value:
        return node
    result = search_bst_value(node.left, value)
    if result is not None:
        return result
    else:
        return search_bst_value(node.right, value)


def search_max_bst(node):  # 이진탐색트리에서 가장 큰 값은 맨 오른쪽에 있다.
    while node != None and node.right != None:
        node = node.right
    return node


def search_min_bst(node):  # 이진탐색트리에서 가장 작은 값은 맨 왼쪽에 있다.
    while node != None and node.left != None:
        node = node.left
    return node


def search_min_bst_recusive(node):
    if node == None:
        return
    else:
        search_min_bst_recusive(node.left)
    return node


def search_max_bst_recusive(node):
    if node == None:
        return
    else:
        search_max_bst_recusive(node.right)
    return node


def insert_bst(root, node):
    if node.key < root.key:
        if root.left is None:
            root.left = node
            return True
        else:
            insert_bst(root.left, node)
    elif node.key > root.key:
        if root.right is None:
            root.right = node
            return True
        else:
            insert_bst(root.right, node)
    else:
        return False


def insert_bst_iter(root, node):
    Rnode = root
    while (Rnode != None):
        if Rnode > node:
            Rnode = Rnode.left  # 왼쪽으로 이동
        elif Rnode < node:
            Rnode = Rnode.right  # 오른쪽으로 이동
        else:  # 같으면 이미 데이터가 존재하므로 삽입하지 않음
            return False  # 삽입하지 않음
    Rnode = node  # Rnode == None이라 while문을 빠져나옴 & 빈 곳에 node값을 삽입
    return True  # 삽입 성공


def delete_bst_case1(parent, node, root):  # 단말노드의 삭제
    if parent is None:  # 삭제할 단말노드의 부모노드가 None이면
        root = None  # 공백트리가 됨
    else:  # 삭제할 노드가 단말노드이므로 그 노드의 부모를 찾아서 왼쪽 오른쪽 탐색 후 삭제
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root  # root가 변경될 수 있으므로 반환


def delete_bst_case2(parent, node, root):  # 자식이 하나인 노드의 삭제
    if parent is None:  # 삭제하려는 노드가 root, root는 자식을 하나만 가지고 있음
        if node.left is None:  # 삭제하려는 노드의 왼쪽이 빈 경우(=오른쪽만 있음)
            root = node.right  # root를 삭제하려는 노드(root)의 자식(node.right)으로 둔다
        elif node.right is None:  # 반대의 경우
            root = node.left
    else:  # 삭제하려는 노드의 부모가 있음
        if parent.left == node:
            if node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left
        elif parent.right == node:
            if node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left
    return root


def delete_bst_case2_modify(parent, node, root):
    # child를 초기화하는 구문, left is not None => left만 존재, left is None => right만 존재
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:  # 삭제노드가 root라면
        root = child  # root를 자식노드(child)로 둠
    else:  # 삭제노드가 root이외의 노드
        if node is parent.left:  # 삭제노드가 부모의 왼쪽이면
            parent.left = child  # 부모의 왼쪽을 삭제노드의 자식으로 둔다.
        else:  # 반대의 경우
            parent.right = child

    return root


def delete_bst_case3(parent, node, root):
    temp_P = node  # 후계자 노드의 부모: 초기값은 node
    temp = node.right  # 후계자 노드: 초기값은 node.right
    # 후계자 노드는 삭제노드의 왼쪽 서브트리의 가장 큰 값 혹은
    # 오른쪽 서브트리의 가장 작은 값으로 두는데 여기서는 후자를 택함

    while temp.left != None:  # 후계자 노드를 찾는다. 즉, 오른쪽 서브트리의 가장 왼쪽 값
        temp_P = temp
        temp = temp.left
    # 이후 temp_P 와 temp는 완전히 후계자노드의 부모와 후계자 노드이다.
    # 계속 왼쪽으로 이동하려 했지만 처음부터 왼쪽 노드가 없는 경우가 생긴다!

    if temp_P.left == temp:  # while구문에서 왼쪽으로 이동할 수 있어 후계자 노드를 잘 찾은 경우
        # 후계자 노드가 오른쪽 서브트리를 가질 수 있기 때문에 후계자 노드의 서브트리를 올려준다.
        temp_P.left = temp.right
    else:  # while구문에서 처음부터 왼쪽 노드가 없는 경우일 때
        # 이때 while문에서 제대로 처리되지 않으므로 실제 값은 node와 node.right이다.
        temp_P.right = temp.right
        # 따라서 node의 오른쪽 자식과 node.right의 오른쪽 자식을 연결해준다.

    # node를 temp로 덮어씌우는 구문
    node.key = temp.key
    node.value = temp.value
    node = temp

    return root


def delete_bst(root, key):
    if root == None:
        return None  # 공백트리인 경우

    parent = None  # 삭제할 노드의 부모노드, 초기값은 None
    node = root  # 삭제할 노드, 초기값은 root

    while node != None and node.key != key:
        parent = node  # parent 값 변경
        if key < node.key:
            node = node.left  # 키값을 서로 비교하여 node 변경
        else:
            node = node.right

    if node == None:
        return None  # 삭제할 노드가 없는 경우

    if node.left == None and node.right == None:  # 단말노드인 경우
        root = delete_bst_case1(parent, node, root)  # case1
    elif node.left == None or node.right == None:  # 유일한 자식을 가진 경우
        root = delete_bst_case2_modify(parent, node, root)  # case2
    else:  # 두개의 자식을 가진 경우
        root = delete_bst_case3(parent, node, root)  # case3
    return root
