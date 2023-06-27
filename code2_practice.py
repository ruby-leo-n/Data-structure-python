# q1
# for i in range(1, 10):
#     print("6x %d=" % i, 6*i)

# q2
# i = 1
# while i < 10:
#     print("6x %d=" % i, 6*i)
#     i += 1

# q3
# for i in range(9, 0, -1):
#     print("6x %d=" % i, 6*i)

# i = 9
# while i >= 1:
#     print("6x %d=" % i, 6*i)
#     i -= 1

# q4
# def change_CtoF(tempC):
#     tempF = tempC*1.8 + 32
#     print("섭씨 온도 %.2f는 화씨 온도 %.2f" % (tempC, tempF))

# change_CtoF(float(input("섭씨 온도를 입력해주세요:")))

# q5
# def change_FtoC(tempF):
#     tempC = (tempF - 32)*0.55
#     print("화씨 온도 %.2f는 섭씨 온도 %.2f" % (tempF, tempC))


# change_FtoC(float(input("화씨 온도를 입력해주세요:")))

# q6
# A = [1, 2, 3, 4, 5]
# for i in range(-1, -6, -1):
#     print(A[i], end=" ")

# q7
# A = [1, 2, 3, 4, 5]
# def sum_listvalues(value):
#     sum = 0
#     for i in range(0, len(A)):
#         sum += A[i]
#     return sum
# print(sum_listvalues(A))

# q8
# msg = "Data Structures in Python"
# print(msg)
# print(msg[::-1])

# q9
# price = {'콩나물 해장국': 4500, '갈비탕': 9000, '돈까스': 8000}
# price["팟타이"] = 7000
# print(price)

# q10
# price = {'콩나물 해장국': 4500, '갈비탕': 9000, '돈까스': 8000}
# for key in price.keys():
#     price[key] -= 500
# print(price)

# q11
# def re_func(n):
#     if n == 1:
#         return 1
#     return re_func(n-1)+n

# print(re_func(10))

# q12
# def re_func(n):
#     if n == 1:
#         return 1
#     else:
#         return re_func(n-1)+(1/n)

# print("%.3f" % (re_func(10)))

# q13
# def re_Bico(n, k):
#     if k == 0 or k == n:
#         return 1
#     elif k > 0 and k < n:
#         return re_Bico(n-1, k-1)+re_Bico(n-1, k)

# print(re_Bico(10, 4))

# def inter_Bico(n, k):
#     result = 1
#     facto = 1
#     if k == 1:
#         return n
#     elif k == 0 or k == n:
#         return result
#     elif 0 < k and k < n:
#         for i in range(n, n-k, -1):
#             result *= i
#         for j in range(1, k+1):
#             facto *= j
#         result = result/facto
#         return result

# print(inter_Bico(10, 4))

# q15
# def reverse(strings):
#     print(strings[::-1])
# reverse("ABCDEFG")

# q16
# def printNum(n):
#     for i in range(1, n+1):
#         print(i, end=" ")
#     print("")

# def printRevNum(n):
#     for j in range(n, 0, -1):
#         print(j, end=" ")

# printNum(10)
# printRevNum(10)
