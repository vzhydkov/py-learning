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
