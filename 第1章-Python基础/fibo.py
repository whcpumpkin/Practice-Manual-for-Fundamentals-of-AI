# 斐波那契数列模块


def fib(n):  # 打印斐波那契数列直到 n
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib2(n):  # 返回斐波那契数列直到 n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
