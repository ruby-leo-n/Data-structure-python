from code4 import Stack


def reverse(expr):
    basket = Stack()
    for term in expr:
        basket.push(term)

    print("re:", end=" ")

    while not basket.isEmpty():
        print(basket.pop(), end="")


expr = input("input:")
reverse(expr)
