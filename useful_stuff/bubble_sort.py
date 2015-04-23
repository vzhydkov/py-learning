"""
Bubblesort is an elementary sorting algorithm.
"""


def bubble_sort(lst):
    """Return the sorted list
    >>> bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    l = len(lst)
    for a in range(l):
        for b in range(l-1):
            if lst[a] < lst[b]:
                lst[a], lst[b] = lst[b], lst[a]
    return lst


if __name__ == "__main__":
    import doctest
    doctest.testmod()

