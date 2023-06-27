# 순차탐색: 테이블이 정렬되어 있지 않다면 순차탐색 이외에 별다른 대안은 없다.
def sequential_search(A, key, low, high):  # 리스트 A와 탐색키 key, 탐색범위 low ~ high
    for i in range(low, high):
        if A[i].key == key:
            return i
    return None

# 이진탐색: 테이블이 정렬되어 있다면 이진탐색을 사용할 수 있다.
# 이진탐색은 매우 효율적인 탐색이지만 탐색하기 전 반드시 배열되어야 한다는 전제가 있다.
# 따라서 데이터의 삽입이나 삭제가 빈번할 경우 적합하지 않다.


def binary_search(A, key, low, high):  # 순환적으로 표현
    if (low <= high):
        middle = (low+high) // 2
        if key == A[middle].key:
            return middle
        elif key < A[middle].key:
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return None


def binry_search_iter(A, key, low, high):
    while (low <= high):
        middle = (low+high) // 2
        if key == A[middle].key:
            return middle
        elif key > A[middle].key:
            low = middle+1
        elif key < A[middle].key:
            high = middle-1
        return None

# 보간탐색: 이진탐색의 일종으로 탐색키가 존재할 위치를 예측하겨 탐색하는 방법
# 이진탐색에서 탐색위치 middle은 (low+high)//2로 항상 절반으로 분할했지만
# 보간탐색에서는 찾고자하는 킷값과 현재의 low,high 위치의 값을 고려하여 다음과 같이 탐색위치를 결정한다.
# 탐색위치 = low+(high-low)*{(k-A[low])/(A[high]-A[low])} k는 찾고자 하는 키값


def inter_search(A, key, low, high):
    while (low <= high):
        middle = int(low+(high-low) *
                     {(key-A[low].key)/(A[high].key-A[low].key)})
        if key == A[middle].key:
            return middle
        elif key > A[middle].key:
            low = middle+1
        elif key < A[middle].key:
            high = middle-1
        return None

# 탐색키가 문자열인 경우는 보통 각 문자에 정수를 대응시켜 바꾸게 된다.
# 각 문자의 아스키 코드나 유니코드 값을 그대로 이용할 수 있다. 가능하면 문자열안으 모든 문자를 골고루 사용하는 것이 좋을 것이다.
# 다음은 제산함수로 문자열을 처리하는 함수이다.


def hashFn(key):
    M = 13  # PrimeNumber
    sum = 0
    for c in key:
        sum = sum+ord(c)
    return sum % M
