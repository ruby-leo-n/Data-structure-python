from code8_2 import MaxHeap
# 최대힙 클래스를 이용항 정렬

# 정렬 과정은 정렬할 항목들을 모두 힙에 넣었다가 순서대로 꺼내는 것
# 이때 최대 힙은 가장 큰 항목부터 출력하므로 오름차순으로 정렬하기 위해서는 힙에서 꺼낸 항목들을 리스트의 맨 뒤에서부터 채워나가야 한다.


def heapSort(data):
    heap = MaxHeap()
    for n in data:
        heap.insert(n)

    heap.display("after heap insert: ")

    for i in range(1, len(data)+1):
        data[-i] = heap.delete()  # 가장 큰 것부터 삭제

    print("after data insert: ", data)

# 시간 복잡도는 힙의 삽입, 삭제 모두 (nlogn)이다. 하지만 이 방법은 추가적인 메모리가 필요하다.
# 즉, 입력 데이터의 모든 항목을 다른 메모리 공간인 힙에 모두 넣었다 빼야 하기 때문이다.
# 입력 데이터의 크기에 비례하는 추가적인 메모리 공간이 필요하다.


def main():
    data = [2, 5, 6, 1, 7, 8, 9, 0, 3, 11, 4, 10]
    heapSort(data)
    for i in range(len(data)):
        print(data[i], end=" ")


if __name__ == '__main__':
    main()
