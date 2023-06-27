# while 구구단
from audioop import reverse


dan = int(input("단을 입력:"))
i = 1
while i < 10:
    print(str(dan) + "*" + str(i) + "=", dan*i)
    i += 1

# range 구구단
ddan = int(input("단을 입력:"))
for k in range(1, 10, 1):
    print(str(ddan)+"*"+str(k)+"=", ddan*k)

# 문자열 for
for c in "game over good bye":
    print("문자:", c)

# 딕셔너리 for
mydict = {'a': 12, 'b': 22, 'c': 56, 'd': 87, 'e': 42}
for d in mydict:
    print("키:", d)
    print("값:", mydict[d])

# 문자열 역순
str1 = "game win or game over choose!"
len = len(str1)
for i in range(0, len, 1):
    print(str1[i])

# 문자열 반복 연산자
print("hi"*60)
