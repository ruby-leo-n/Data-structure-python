from code4 import Stack


def precedence(op):  # 연산자 우선 순위 반환
    if op == "(" or op == ")":
        return 0
    elif op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    else:
        return -1

# 왼쪽 괄호를 만나면 스택에 넣는다.
# 피연산자는 바로 출력한다.
# 오른쪽 괄호가 나오면 왼쪽 괄호가 나올 때까지 모든 연산자를 꺼내 출력한다.
# 처리가 끝났으면 스택에 있는 연산자를 모두 출력한다.


def Infix2Postfix(expr):  # 중위에서 후위로 변환 expr에는 전위표기식으로 되어있음
    s = Stack()  # 스택: 연산자 보관
    output = []  # 후위표기식 리스트 & 출력
    for term in expr:
        if term in "(":
            s.push("(")
        elif term in ")":
            while not s.isEmpty():
                op = s.pop()
                if op == "(":
                    break
                else:
                    output.append(op)
        elif term in "+-*/":  # 연산자
            while not s.isEmpty():
                op = s.peek
                if (precedence(term) <= precedence(op)):  # 우선순위가 높거나 같은 연산자를 모두 출력
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:  # 피연산자
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output


infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)

print("중위표기: ", infix1)
print("후위표기: ", postfix1)
print("------")
print("중위표기: ", infix2)
print("후위표기: ", postfix2)
