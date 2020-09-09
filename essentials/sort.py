def bubble_sort(lst):
    """
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> bubble_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def selection_sort(lst):
    """
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> selection_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    for i in range(len(lst)-1, 0, -1):
        max_val = 0
        for k in range(1, i+1):
            if lst[k] > lst[max_val]:
                max_val = k
        lst[i], lst[max_val] = lst[max_val], lst[i]


def insertion_sort(lst):
    """
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> insertion_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    for i in range(1, len(lst)):
        val = lst[i]
        pos = i
        while pos > 0 and lst[pos-1] > val:
            lst[pos] = lst[pos-1]
            pos = pos-1
        lst[pos] = val


if __name__ == "__main__":
    import doctest
    doctest.testmod()
