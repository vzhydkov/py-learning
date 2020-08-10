def fibonacci_loop(n):
    """
    >>> fibonacci_loop(16)
    987
    """
    if n <= 0:
        return 0
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def fibonacci_recursion(n):
    """
    >>> fibonacci_recursion(16)
    987
    """
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


def fibonacci_generator(n):
    """
    >>> list(fibonacci_generator(16))[-1]
    987
    """
    if n <= 0:
        yield 0
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


def fibonacci_memoization(n, memo={}):
    """
    Best approach:
    Time complexity: O(n)
    Space complexity: O(n)
    >>> fibonacci_memoization(16)
    987
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if not memo.get(n):
        memo[n] = fibonacci_memoization(n - 2) + fibonacci_memoization(n - 1)
    return memo[n]


def factorial_loop(n):
    """
    >>> factorial_loop(16)
    20922789888000
    """
    if n < 0:
        raise Exception('must be greater than or equal to zero')
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def factorial_while(n):
    """
    >>> factorial_while(16)
    20922789888000
    """
    if n < 0:
        raise Exception('must be greater than or equal to zero')
    res = 1
    while n >= 1:
        res = res * n
        n = n - 1
    return res


def factorial_recursion(n):
    """
    >>> factorial_recursion(16)
    20922789888000
    """
    if n < 0:
        raise Exception('must be greater than or equal to zero')
    if n == 0:
        return 1
    return n * factorial_recursion(n-1)


def factorial_generator(n):
    """
    >>> list(factorial_generator(16))[-1]
    20922789888000
    """
    if n < 0:
        raise Exception('must be greater than or equal to zero')
    res = 1
    for i in range(2, n+1):
        res *= i
        yield res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
