def qs(alist):
    _qs(alist, 0, len(alist) - 1)


def _qs(alist, start, end):
    if start < end:
        split_pos = partition(alist, start, end)
        _qs(alist, 0, split_pos - 1)
        _qs(alist, split_pos + 1, end)


def partition(alist, start, end):
    partition_value = alist[start]
    left = start + 1
    right = end
    while 1:
        while left <= right and partition_value >= alist[left]:
            left += 1
        while left <= right and partition_value <= alist[right]:
            right -= 1
        if right < left:
            break
        else:
            alist[left], alist[right] = alist[right], alist[left]

    alist[start], alist[right] = alist[right], alist[start]
    return right


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
qs(alist)
print(alist)
