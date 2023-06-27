# time 라이브러리로 알고리즘 시간 측정
import time
import math

start = time.time()
math.factorial(9999)
end = time.time()
print("실행시간=", end - start)


# 재귀로 구현한 팩토리얼 함수
def facto_recusive(n):
    if n == 1:
        return 1
    else:
        return n*facto_recusive(n-1)


print("재귀로 구한 팩토리얼값은", facto_recusive(10))


# 반복으로 구현한 팩토리얼 함수
def facto_inter(n):
    result = 1
    for k in range(n, 0, -1):
        result = result*k
    return result


print("반복으로 구한 팩토리얼값은", facto_inter(10))


# 재귀가 더 빠른 경우: 거듭제곱 구하기
def power_inter(x, n):
    result = 1
    for i in range(n):
        result = result*x
    return result


def power_recusive(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_recusive(x*x, n//2)
    else:
        return x*power_recusive(x*x, (n-1)//2)


print("재귀:", power_recusive(6, 12))
print("반복:", power_inter(6, 12))


# 재귀가 느린 경우가 많다: 피보나치 수열
def fib_recusive(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib_recusive(n-2)+fib_recusive(n-1)


def fib_inter(n):
    last = 0
    tmp = 1
    if n < 2:
        return n
    else:
        for i in range(2, n+1):
            front = last+tmp
            last = tmp
            tmp = front
        return front


print("재귀 피보나치 수열:", fib_recusive(20))
print("반복 피보나치 수열:", fib_inter(20))


# 하노이의 탑 재귀함수

def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print("원판1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판%d: %s --> %s" % (n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)


hanoi_tower(4, 'A', 'B', 'C')
