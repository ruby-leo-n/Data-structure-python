# 답지 참고 반드시 복기해볼것!
import heapq
from heapq import heappop, heappush


def isLeaf(root):
    return root.left is None and root.right is None


# A 트리 노드
class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    # `__lt__()` 함수를 재정의하여 `Node` 클래스가 우선 순위 대기열과 함께 작동하도록 합니다.
    # 가장 높은 우선순위 항목이 가장 낮은 빈도를 갖도록
    def __lt__(self, other):
        return self.freq < other.freq


# 허프만 트리를 탐색하고 사전에 허프만 코드를 저장
def encode(root, s, huffman_code):

    if root is None:
        return

    # 리프 노드를 찾았습니다.
    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)


# 허프만 트리를 탐색하고 인코딩된 문자열을 디코딩합니다.
def decode(root, index, s):

    if root is None:
        return index

    # 리프 노드를 찾았습니다.
    if isLeaf(root):
        print(root.ch, end='')
        return index

    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)


# 허프만 트리를 구축하고 주어진 입력 텍스트를 디코딩합니다
def buildHuffmanTree(text):

    # 기본 케이스: 빈 문자열
    if len(text) == 0:
        return

    # 각 캐릭터의 출현 빈도를 계산합니다.
    # 사전에 저장
    freq = {i: text.count(i) for i in set(text)}

    # Huffman 트리의 라이브 노드를 저장할 우선 순위 대기열를 만듭니다.
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    # Queue에 노드가 둘 이상 있을 때까지 수행
    while len(pq) != 1:

        # 우선 순위가 가장 높은 두 노드를 제거합니다.
        # Queue에서 #(최저 주파수)

        left = heappop(pq)
        right = heappop(pq)

        #  이 두 노드를 자식으로 사용하여 새 내부 노드를 만들고
        #  두 노드의 주파수 합과 동일한 주파수를 사용합니다.
        # 우선 순위 대기열에 새 노드를 추가합니다.

        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))

    # `root` 는 허프만 트리의 루트에 대한 포인터를 저장합니다.
    root = pq[0]

    # Huffman 트리를 탐색하고 Huffman 코드를 사전에 저장합니다.
    huffmanCode = {}
    encode(root, '', huffmanCode)

    # 허프만 코드 인쇄
    print('Huffman Codes are:', huffmanCode)
    print('The original string is:', text)

    # 인코딩된 문자열을 인쇄합니다.
    s = ''
    for c in text:
        s += huffmanCode.get(c)

    print('The encoded string is:', s)
    print('The decoded string is:', end=' ')

    if isLeaf(root):
        # 특수 케이스: a, aa, aaa 등과 같은 입력용
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1
    else:
        # 이번에도 허프만 트리를 횡단하고,
        # 인코딩된 문자열 디코딩
        index = -1
        while index < len(s) - 1:
            index = decode(root, index, s)


# Python에서 허프만 코딩 알고리즘 구현
if __name__ == '__main__':

    text = 'Huffman coding is a data compression algorithm.'
    buildHuffmanTree(text)
