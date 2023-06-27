# is 연산자
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)

# 기본 연산자
print("2**5=", 2**5)
print("14/5=", 14/5)
print("14//5=", 14//5)

# in 연산자
print('a' in 'banna')
print('seed' in 'banna')

A = [1, 2, 3, 4, 5, 7]
if 3 in A:
    print("true")

while 4 in A:
    print("true")
    break

# input 함수
name = input("name:")
hobby = input("hobby:")
age = int(input("age:"))
high = float(input("high:"))

# line feed
print("game", end=" ")
print("over")

# 이스케이프 시퀀스
print("\\\n반갑\t습니다\"")

# 튜플
msg1 = "당신의 이름%s이며 취미는 %s입니다." % (name, hobby)
msg2 = "당신의 나이는%d이며 키는 %3.1f입니다." % (age, high)

print(msg1)
print(msg2)
