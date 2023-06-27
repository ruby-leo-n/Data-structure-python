import heapq


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


def heapSort(arr):
    n = len(arr)
    print("before sort: %2s" % (""), arr)
    heapq._heapify_max(arr)
    print("after heapify: %0s" % (""), arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("%7si = %3s " % ("", i), arr)


def main():
    data = [2, 5, 6, 1, 7, 8, 9, 0, 3, 11, 4, 10]
    heapSort(data)
    print("after sort:%4s" % (""), data)


if __name__ == '__main__':
    main()
