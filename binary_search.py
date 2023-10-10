from bisect import bisect
from random import randint


def binary_search(array, item):
    '''возвращает индекс в массиве либо None'''
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_insert(array, item):
    '''возвращает индекс для вставки элемента'''
    low = 0
    high = len(array)
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return low


def binary_search_leftmost(array: list, value):
    left = 0
    right = len(array) - 1
    while left < right:
        middle = (left + right) // 2
        middle_value = array[middle]
        if middle_value < value:
            left = middle + 1
        else:
            right = middle

    if array[left] == value:
        return left
    else:
        return None


def binary_search_rightmost(array: list, value):
    left = 0
    right = len(array)
    while left < right:
        middle = (left + right) // 2
        middle_value = array[middle]
        if middle_value > value:
            right = middle
        else:
            left = middle + 1

    if array[right - 1] == value:
        return right - 1
    else:
        return None


def r_binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    if (val == arr[mid]):
        return mid
    if (val > arr[mid]):
        return binary_search(arr[mid + 1:], val) + (mid + 1)
    return binary_search(arr[:mid], val)


def bisect_(sequence: list, x: int):
    """return i:  all(val <= x for val in sequence[lo : i]) for the left side and all(val > x for val in sequence[i : hi])"""
    left = 0
    right = len(sequence)
    while left < right:
        middle = (left + right) // 2

        if sequence[middle] > x:
            right = middle
        else:
            left = middle + 1

    return right


# def search_closest_to_x(sequence: list, x: int):
#     left = 0
#     right = len(sequence) - 1



if __name__ == '__main__':
    def test_bisect():
        for _ in range(100000):
            n = randint(1, 10)
            seq = [randint(-100, 100) for i in range(n)]
            seq.sort()
            # print(seq)

            x = randint(-100, 100)
            # print(x)
            if bisect_(seq, x) != bisect(seq, x):
                print("WA")
                break


    # a = [1, 3, 5, 7, 9, 11, 13]
    b = [1, 3, 5, 7, 9, 11]
    b1 = [1, 3, 5, 7, 9, 11]
    b2 = [1, 3, 5, 7, 9, 11]
    # print(r_binary_search(a, 11))
    # print(binary_search(a, 3))
    # print(binary_insert(a, 6))
    # print(bisect_(b,9))
    # print(bisect_(b,2))
    # print(bisect_(b,10))
    test_bisect()
    # print(bisect_([-97, -79, -38, -6, 5, 60, 96, 96], 96))
    # print(bisect_([-66, -49, -21, 2, 18], -49))
    # seq1 = [3, 3, 3, 5, 6, 7, 8, 9, 9]
    # seq2 = [1, 1, 2, 2, 3, 3, 3, 5, 6, 7, 8, 9, 9]
    seq3 = [1, 1, 2, 2, 3, 3, 3, 5, 6, 7, 8, 9, 9, 9, 9]
    # print(binary_search_rightmost(seq1, 3))
    # print(binary_search_rightmost(seq2, 3))
    # print(binary_search_rightmost(seq3, 9))
    # print(binary_search_rightmost(seq3, 5))
