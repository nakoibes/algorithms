def merge(a, b):
    c = []
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if a:
        c.extend(a)
    elif b:
        c.extend(b)
    return c


def merge_sort(array: list):
    size = len(array)
    if size == 1:
        return array
    middle = (size - 1) // 2
    left_half = array[:middle + 1]
    right_half = array[middle + 1:]
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return merge(sorted_left, sorted_right)


if __name__ == '__main__':
    array2 = [5, 1, 45, 100, 4, 46, 78, 22, 11]
    a = [1, 5, 7, 10]
    b = [1, 2, 3, 4, 5, 6]
    c = []
    # print(c)
    print(merge_sort(array2))
