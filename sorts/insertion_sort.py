def insertion_sort(array: list):
    size = len(array)
    for i in range(1, size):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def insertion_sort_recursion(array: list, left: int, right: int) -> None:
    """just replacing outer loop"""
    size_ = right - left
    if size_ == 0:
        return
    insertion_sort_recursion(array, left, right - 1)
    j = right - 1
    key = array[right]
    while j >= left and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j+1] = key


if __name__ == '__main__':
    array = [5, 1, 45, 100, 4, 46, 78, 22, 11]
    # print(insertion_sort(array))
    print(insertion_sort_recursion(array, 0, len(array) - 1))
    print(array)
