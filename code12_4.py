def merge_sort(A, left, right):
    if left < right:
        mid = (left+right)//2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    k = left  # 정렬된 배열의 왼쪽 인덱스
    i = left  # left에서 mid까지 배열의 왼쪽 인덱스
    j = mid + 1  # mid+1에서 right까지 배열의 왼쪽 인덱스
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1
    if i > mid:
        sorted[k:k+right-j+1] = A[j:right+1]
    elif j > right:
        sorted[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1] = sorted[left:right+1]


def main():
    global sorted
    sorted = []
    test = [2, 5, 6, 1, 7, 8, 9, 0, 3, 11, 4, 10]
    sorted = [0]*len(test)
    merge_sort(test, 0, len(test)-1)
    print("merge Sort", test)


if __name__ == '__main__':
    main()
