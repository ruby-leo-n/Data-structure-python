from queue import Queue
BUCKETS = 10
DIGITS = 4


def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor) % 10].put(A[i])
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                i += 1
        factor *= 10
        print("     step", d+1, A)


def main():
    import random
    test = []
    for i in range(10):
        test.append(random.randint(1, 9999))
    print("data      :", test)
    radix_sort(test)
    print("radix Sort:", test)


if __name__ == '__main__':
    main()
