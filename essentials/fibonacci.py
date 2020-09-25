def fibonacci_loop(n):
    """
    >>> fibonacci_loop(16)
    987
    """
    if n < 0:
        raise ValueError('Negative arguments not implemented')
    if n == 0:
        return 0
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def fibonacci_generator(n):
    """
    >>> list(fibonacci_generator(16))[-1]
    987
    """
    if n < 0:
        raise ValueError('Negative arguments not implemented')
    if n == 0:
        yield 0
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


def fibonacci_recursion(n):
    """
    >>> fibonacci_recursion(16)
    987
    """
    if n < 0:
        raise ValueError('Negative arguments not implemented')
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


def fibonacci_memoization(n, memo={}):
    """
    Dynamic Programming
    Time complexity: O(n)
    Space complexity: O(n)
    >>> fibonacci_memoization(16)
    987
    """
    if n < 0:
        raise ValueError('Negative arguments not implemented')
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if not memo.get(n):
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]


def fibonacci_fast_doubling(n):
    """
    Divide-and-conquer algorithm
    Time complexity: O(log(n))
    >>> fibonacci_fast_doubling(16)
    987
    """
    def _fibonacci(i):
        if i == 0:
            return 0, 1
        else:
            a, b = _fibonacci(i // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if i % 2 == 0:
                return c, d
            else:
                return d, c + d
    if n < 0:
        raise ValueError('Negative arguments not implemented')
    return _fibonacci(n)[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
