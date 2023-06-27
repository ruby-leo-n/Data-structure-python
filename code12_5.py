def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q-1)
        quick_sort(A, q+1, right)


def partition(A, left, right):
    low = left+1
    high = right
    pivot = A[left]

    while low <= high:  # low는 증가 high는 감소 시키므로 역전되기 전까지 반복
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]  # 역전 된 경우 종료하고 high와 피벗이된 left를 교환한다.
    return high  # 피벗위치 반환


def main():
    test = [2, 5, 6, 1, 7, 8, 9, 0, 3, 11, 4, 10]
    quick_sort(test, 0, len(test)-1)
    print("quick Sort", test)


if __name__ == '__main__':
    main()

# 최악의 경우는 리스트가 불균형하게 있는 것이다.
# 불균형 분할을 완화하기 위해 피벗을 리스트의 중앙값으로 설정해둔다.
