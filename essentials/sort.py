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
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            # Update minimum index
            if lst[j] < lst[min_index]:
                min_index = j
        # Swap current index with minimum element in rest of list
        lst[min_index], lst[i] = lst[i], lst[min_index]


def insertion_sort(lst):
    """
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> insertion_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    for i in range(1, len(lst)):
        pos = i
        val = lst[i]
        while pos > 0 and lst[pos-1] > val:
            lst[pos] = lst[pos-1]
            pos -= 1
        lst[pos] = val


def merge_sort(lst):
    """
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> merge_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    def merge(lst, left, right):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    if len(lst) <= 1:
        return
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(lst, left, right)


def quick_sort(lst):
    """
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> quick_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    def partition(lst, start, end):
        follower = leader = start
        while leader < end:
            if lst[leader] <= lst[end]:
                lst[follower], lst[leader] = lst[leader], lst[follower]
                follower += 1
            leader += 1
        lst[follower], lst[end] = lst[end], lst[follower]
        return follower

    def sort(lst, start, end):
        if start >= end:
            return
        index = partition(lst, start, end)
        sort(lst, start, index - 1)
        sort(lst, index + 1, end)

    sort(lst, 0, len(lst) - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
