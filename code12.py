def shell_sort(arr):
    n = len(arr)
    gap = n//2  # gap을 리스트 크기의 절반으로 초기화 함

    while gap > 0:
        if gap % 2 == 0:  # 짝수인 경우 홀수로 gap을 설정함
            gap += 1
        for i in range(gap):  # gap은 부분리스트의 갯수와 동일함
            sortGapInsertion(arr, i, n-1, gap)
        print(" Gap = ", gap, arr)
        gap = gap//2  # gap을 절반으로 나눔


def sortGapInsertion(arr, first, last, gap):
    for i in range(first+gap, last+1, gap):  # 부분 리스트의 갯수만큼 반복 (first+gap) - (last+1) = gap
        key = arr[i]
        j = i - gap  # 리스트의 뒤를 먼저 구하고 앞으로 진행하여 항목을 찾음
        while j >= first and key < arr[j]:  # 리스트 범위 내에서 key보다 큰 항목이 있다면
            arr[j+gap] = arr[j]  # key 보다 더 큰 항목을 뒤로 보냄. 당연히 gap만큼 차이를 둠
            j = j-gap  # j를 앞으로 진행시킴
        arr[j+gap] = key  # while문에서 빠져 나와 key의 올바른 위치에 삽입


def main():
    text = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("original:", text)
    shell_sort(text)
    print("   shell:", text)


if __name__ == '__main__':
    main()
