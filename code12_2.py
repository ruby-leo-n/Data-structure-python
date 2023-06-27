# 제자리 정렬로 구현한 힙 정렬
# 힙 정렬을 추가적인 메로리를 사용하지 않는 제자리 정렬 방식으로도 구현할 수 있다.
# 방법은 입력 배열 자체를 최대 힙으로 먼저 만들고, 다음으로 오름차순으로 정렬시키는 방법이다.

# 정렬되지 않은 배열을 최대 힙으로
# 정렬되지 않은 배열을 최대 힙으로 만드는 과정은 배열의 맨 뒤쪽 항목부터 시작해서 앞으로 가면서 힙 조건을 만족시킨다.
# 하지만 힙 트리에서 형제노드끼리는 힙 조건이 필요없므로 이미 힙을 이루고 있다고 생각할 수 있다.

# heapify함수는 현재 위치 i으 왼쪽 자식과 오른쪽 자식 중에서 더 큰 자식이 자신보다 크면 자신과 더 큰 자식을 교환하고
# 재귀호출을 이용하여 더 큰 자식에게 다시 이 과정을 반복한다.
# 이 과정을 더 이상 교환이 없을 때까지 진행한다.

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# 최대힙을 정렬된 배열로
# heapify함수를 통해 최대힙이 완성되었지만 최대 힙이 만들어졌다고 정렬된 것은 아니다.
# 이제 최대 힙에서 항목들을 하나씩 꺼내 순서대로 저장해야 정렬이 완성된 것이다.

# 힙의 삭제는 루트를 삭제하는 것이다. 따라서 루트의 숫자를 힙의 마지막 숫자와 교환하고 힙 크기를 1 줄인다.
# 이 상태는 힙 조건을 만족하지 않을 수 있으므로 다운힙 연산으로 반드시 힙을 복원해야 한다.
# 이 과정을 반복하면 모든 원소들이 정렬되고 이때 앞에서 구현한 heapify함수를 다시 이용한다.

def heapSort(arr):
    n = len(arr)
    print("i = ", 0, arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        print("i = ", i, arr)
    print()

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("i = ", i, arr)


def main():
    test = [2, 5, 6, 1, 7, 8, 9, 0, 3, 11, 4, 10]
    heapSort(test)
    print("heap Sort", test)


if __name__ == '__main__':
    main()


# 제자리에서 구현된 힙 정렬의 시간 복잡도 역시 nlogn이다.
# 힙 정렬의 장점은 최악의 경우에도 nlogn으로 제한되고 제자리 정렬이 가능해서 메모리가 추가적으로 필요하지 않다라는 점이다.
