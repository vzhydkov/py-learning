def fibonacci(n):
    """Return the sorted list
    >>> fibonacci(16)
    987
    """
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def fibonacci_recursion(n):
    """Return the sorted list
    >>> fibonacci_recursion(16)
    987
    """
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


def fibonacci_generator(n):
    """Return the sorted list
    >>> list(fibonacci_generator(16))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    """
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


def factorial(n):
    """Return the sorted list
    >>> factorial(16)
    20922789888000
    """
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def factorial_while(n):
    """Return the sorted list
    >>> factorial(16)
    20922789888000
    """
    res = 1
    while n >= 1:
        res = res * n
        n = n - 1
    return res


def factorial_recursion(n):
    """Return the sorted list
    >>> factorial(16)
    20922789888000
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
