# 이중피벗 퀵 정렬은 퀵 정렬을 보완하여 2개의 피벗을 사용하는 퀵 정렬이다.
# 다음과 같이 먼저 리스트의 양쪽 끝에서 두 피벗을 선택하고, 왼쪽 피벗이 오른쪽보다 항상 크지 않도록 조정한 다음 이들을 중심으로 파트를 나누고 퀵 정렬과 같이 반복한다.

# j는 왼쪽 피벗보다 작지 않은 최대 인덱스+1이고, g는 오른쪽 피벗보다 크지 않은 최소 인덱스-1을 나타낸다.
# k를 하나씩 증가시키며서 조건에 따라 항목들을 교환하고 j와 g를 갱신하는 방법으로 분할이 이루어진다.

# 이중피벗 퀵 정렬은 퀵 정렬과 이론 적인 시간복잡도는 차이가 없고 최악의 경우 시간복잡도도 n^2으로 좋지 않다
# 그러나 일반적인 경우 퀵 정렬보다 성능이 우수하다고 알려져있어 자바나 안드로이드 시스템 정렬로 사용되었다.

def dp_quick_sort(A, low, high):
    if low < high:
        lp, rp = partitionDP(A, low, high)
        dp_quick_sort(A, low, lp-1)
        dp_quick_sort(A, lp+1, rp-1)
        dp_quick_sort(A, rp+1, high)


def partitionDP(A, low, high):
    if A[low] > A[high]:
        A[low], A[high] = A[high], A[low]  # 오른쪽 피벗은 왼쪽보다 작지 않아야 한다.

    j = low+1
    g = high-1
    k = low+1

    lpval = A[low]
    rpval = A[high]

    while k <= g:  # k와 g가 역전되면 종료된다.
        if A[k] < lpval:  # 현재 탐색 값이 왼쪽 피벗보다 작은  경우
            A[k], A[j] = A[j], A[k]  # 교환
            j += 1  # 이동

        elif A[k] >= rpval:  # 현재 탐색 값이 오른쪽 피벗보다 큰 경우
            while (A[g] > rpval and k < g):  # 오른쪽 피벗보다 작거나 같은 A[g]를 탐색
                g -= 1  # 이동
            A[k], A[g] = A[g], A[k]  # 교환
            g -= 1  # 이동

            if (A[k] < lpval):  # 이동 후 왼쪽 보다 작으면
                A[k], A[j] = A[j], A[k]  # 교환
                j += 1  # 이동
        k += 1  # k는 순차적으로 방문
    j -= 1
    g += 1
    A[low], A[j] = A[j], A[low]  # j 와 g는 low와 high의 자리이므로 교환한다.
    A[high], A[g] = A[g], A[high]

    return j, g  # 재귀호출하기 때문에 반환


def main():
    test = [2, 5, 6, 1, 7, 8, 9, 0, 3, 11, 4, 10]
    dp_quick_sort(test, 0, len(test)-1)
    print("dp_quick Sort", test)


if __name__ == '__main__':
    main()
