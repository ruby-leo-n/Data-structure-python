MAX_VAL = 100


def counting_sort(A):
    output = [0] * MAX_VAL
    count = [0] * MAX_VAL

    for i in A:
        count[i] += 1

    for i in range(MAX_VAL):
        count[i] += count[i-1]
        # count를 더할 때 뒤의 값에서 앞으로 추가하는 식으로 더해오는데
        # 맨 뒷자리에 MAX_VAL-1의 값이 오면 더할 때 count[0] += count[-1]이 되어버리므로
        # 데이터에서는 0의 값이 존재하지 않는데 갑자기 생겨버림
        # 그래서 전체 데이터가 뒤로 한칸씩 밀려져서 복사* 파트에서 99가 출려되지 않음

    # 오류: data의 맨 마지막에 MAX_VAL-1의 값이 오면 0이 생겨버림
    # data         : [30, 62, 35, 95, 97, 37, 18, 14, 58, 99] 인 경우
    # counting Sort: [0, 14, 18, 30, 35, 37, 58, 62, 95, 97]가 됨

    for i in range(len(A)):
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1

    for i in range(len(A)):
        A[i] = output[i]  # 복사*


def main():
    import random
    org = [random.randint(0, MAX_VAL-1) for _ in range(10)]
    test = list(org)
    print("data         :", test)
    counting_sort(test)
    print("%s" % ("-")*100)
    print("counting Sort:", test)


if __name__ == '__main__':
    main()
