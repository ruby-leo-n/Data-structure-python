from code4 import Stack

main = Stack()
sub = Stack()
global check
check = 0


def input(item):
    main.push(item)


def delete(num):  # 삭제하는 횟수
    global check
    for i in range(num):
        check += 1


def downgrade():
    global check
    for i in range(main.size()-(check+1)):  # check이후로 존재하는 원소갯수만큼 실행
        main.top[i] = main.top[check+1+i]  # 뒤에서 앞으로 옮김
    # check이후로 불필요한 부분을 완전제거한다.
    del main.top[main.size()-(check+1): main.size()]
    check = 0


def output():
    if (check >= 3):  # 나중에 main의 공간복잡도가 많아진다.
        downgrade()  # main의 공간복잡도를 줄이기 위해서 downgrade함수 실행
        for i in range(check, main.size()):
            sub.push(main.top[-(i+1)])
        for i in range(check, main.size()):  # check에서 main.size까지 즉, check이후로 원소갯수
            print(sub.top[-(i+1)], end=" ")
        sub.top.clear()  # 출력완료 후 sub스택을 전부 지운다.
        print()
    else:
        for i in range(check, main.size()):
            sub.push(main.top[-(1+i)])
        for i in range(check, main.size()):
            print(sub.top[-(1+i)], end=" ")
        sub.top.clear()
        print()


for i in range(10):
    input(i)

output()

delete(3)

output()
