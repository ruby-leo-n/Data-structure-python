# 삽입정렬 알고리즘
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):  # 1부터 리스트의 끝까지
        key = A[i]
        j = i-1
        while (j >= 0 and A[j] > key):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A, i)


def printStep(arr, val):
    print(" Step %2d = " % val, end="")
    print(arr)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("original:", data)
insertion_sort(data)
print("selection:", data)
