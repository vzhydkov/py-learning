from typing import List


def factorial_loop(n: int) -> int:
    """
    >>> factorial_loop(16)
    20922789888000
    """
    if n < 0:
        raise Exception('Must be greater than or equal to zero')
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def factorial_generator(n: int) -> List[int]:
    """
    >>> list(factorial_generator(16))[-1]
    20922789888000
    """
    if n < 0:
        raise Exception('Must be greater than or equal to zero')
    res = 1
    for i in range(2, n+1):
        res *= i
        yield res


def factorial_while(n: int) -> int:
    """
    >>> factorial_while(16)
    20922789888000
    """
    if n < 0:
        raise Exception('Must be greater than or equal to zero')
    res = 1
    while n >= 1:
        res = res * n
        n = n - 1
    return res


def factorial_recursion(n: int) -> int:
    """
    >>> factorial_recursion(16)
    20922789888000
    """
    if n < 0:
        raise Exception('Must be greater than or equal to zero')
    if n == 0:
        return 1
    return n * factorial_recursion(n-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
