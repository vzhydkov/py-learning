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


def factorial_loop(n):
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


def factorial_generator(n):
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


def factorial_while(n):
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


def factorial_recursion(n):
    """
    >>> factorial_recursion(16)
    20922789888000
    """
    if n < 0:
        raise Exception('Must be greater than or equal to zero')
    if n == 0:
        return 1
    return n * factorial_recursion(n-1)


def multiply_karatsuba(x, y):
    """
    Karatsuba algorithm
    Time complexity: O(log n)
    >>> multiply_karatsuba(1234, 5678)
    7006652
    """
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2

        a, b = divmod(x, 10 ** nby2)
        c, d = divmod(y, 10 ** nby2)

        ac = multiply_karatsuba(a, c)
        bd = multiply_karatsuba(b, d)
        ad_bc = multiply_karatsuba(a + b, c + d) - ac - bd
        return ac * 10 ** (2 * nby2) + (ad_bc * 10 ** nby2) + bd


if __name__ == "__main__":
    import doctest
    doctest.testmod()
