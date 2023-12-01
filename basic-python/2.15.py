def fib(num: int) -> int:
    """
    :param num: order number of fibonacci
    return: int
    """
    if num <= 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)
num = int(input())
print(fib(num))