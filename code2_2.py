# split와 strip
import random
from math import floor, sqrt
import math
str1 = "         hi my name is ji hun kim          "
str2 = "wwwwwwwwwwwwwhi my name is ji hun kimwwwwwwwwwwwww"
str3 = "hi my name is ji hun kim"
print(str1.strip())
print(str2.strip("w"))
print(str3.split("i"))
print(str3.split())

# list
list_ex = ["23", "56", "74", "다음", "kow", "sp", "52"]
list_ex.append("85")
print(list_ex)
list_ex.insert(2, "네이버")
print(list_ex)
list_ex.reverse()
print(list_ex)
list_ex.sort()
print(list_ex)

# 튜플
hobby = 3
name = "김지훈"
high = 177.7
print("취미 갯수 = %d, 이름 = %s, 키 = %3.1f" % (hobby, name, high))

# dict
map = {'김연아': '피겨', '류현진': '야구', '박태환': '수영', '메시': '축구'}
print(map)
map['나달'] = '테니스'
print(map)
map.update({'아사다 마오': '피겨', '손흥민': '축구'})
print(map)

print(map.keys())
print(map.values())

s1 = set([])
s2 = {1, 2, 3}
s3 = {2, 3, 4, 5}
s4 = s2.union(s3)
s5 = s3.intersection(s2)
s6 = s2-s3
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)
print("s5:", s5)
print("s6:", s6)

s1.update({4, 3, 4})
print(s1)

# 사용자 정의 함수


def find_min_max(data):
    min = data[0]
    max = data[0]
    for i in range(1, len(data), 1):
        if min > data[i]:
            min = data[i]
        if max < data[i]:
            max = data[i]
    return max, min


data = [4, 5, 7, 9, 11, 20, 4, 63, 8, 45, 12, 3, 68, 99]
x, y = find_min_max(data)
print("max:", x, "min:", y)


def sum_range(begin, end, step=1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum


print("sum:", sum_range(1, 10))
print("sum:", sum_range(1, 10, 2))


print("sum:", sum_range(step=3, begin=1, end=10))


def calc_perimeter(radius):
    global perimeter
    print("pi value:", pi)
    perimeter = 2*pi*radius


pi = 3.14159
perimeter = 0
calc_perimeter(10)
print("원둘레(r=10):", perimeter)


#import math
result = math.pow(2, 10)
print("result(2^10):", result)


#from math import floor, sqrt
floor_result = floor(45.1214)
sqrt_result = sqrt(121)
print("floor_result:", floor_result)
print("sqrt_result:", sqrt_result)


def random_pop(randpop_data):
    number = random.randint(0, len(randpop_data)-1)
    return randpop_data.pop(number)


randpop_data = list()

if __name__ == "__main__":
    for i in range(1, 46):
        randpop_data.append(i)
    while randpop_data:
        print(random_pop(randpop_data))
