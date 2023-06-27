# 버블정렬 알고리즘
def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if (A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True

        if not bChanged:
            break  # 교환이 발생하지 않으면 False가 바로 내려와서 종료됨
        printStep(A, n-i)


def printStep(arr, val):
    print(" Step %2d = " % val, end="")
    print(arr)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("original:", data)
bubble_sort(data)
print("selection:", data)
