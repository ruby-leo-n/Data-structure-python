from code4 import Stack


def palin(expr):
    stack = Stack()
    put = []
    count = 0
    for term in expr:
        if (term in "./- "):
            count += 1
            continue
        else:
            stack.push(term)
            put.append(term)

    for i in range(len(expr)-count):
        spop = stack.pop()
        if (spop != put[i]):
            return False
    return True


expr = input("input:")
print(palin(expr))
