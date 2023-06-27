from code8 import TNode

# 결정트리
table = [("A", ".-"), ("B", "-..."), ("C", "-.-"), ("D", "-.."),
         ("E", "."), ("F", "..-."), ("G", "--."), ("H", "...."),
         ("I", ".."), ("J", ".---"), ("K", "-.-"), ("L", ".-..."),
         ("M", "--"), ("N", "-."), ("O", "---"), ("P", ".--."),
         ("Q", "--.-"), ("R", ".-."), ("S", "..."), ("T", "-"),
         ("U", "..-"), ("V", "...-"), ("W", ".---"), ("X", "-..-"),
         ("Y", "-.--"), ("Z", "--..")]


def make_more_tree():
    root = TNode(None, None, None)
    for tp in table:  # 반복하여 talbe에 있는 임의의 모르스 부호를 가져옴
        code = tp[1]  # 모르스 부호를 code에 저장
        node = root  # node를 head를 가리키는 포인터로 설정
        for c in code:  # 모르스부호의 .과 -을 따라가면서 반복하여 트리를 생성한다.
            if c == ".":
                if node.left == None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == "-":
                if node.right == None:
                    node.right = TNode(None, None, None)
                node = node.right
        node.data = tp[0]
    return root


def decode(root, code):
    node = root
    for c in code:
        if c == ".":
            node = node.left
        elif c == "-":
            node = node.right
    return node.data


def encode(ch):
    idx = ord(ch)-ord("A")
    return table[idx][1]


morseCodeTree = make_more_tree()
str = input("입력할 문장:")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("morse Code:", mlist)
print("Decoding:", end=" ")
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end="")
print()
