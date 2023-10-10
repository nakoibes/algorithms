def bubble_sort(array: list):
    size = len(array)
    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array


def bubble_sort_optimized(array: list):
    size = len(array)
    while size > 0:
        last_swap = 0
        for j in range(size - 1):
            if array[j] > array[j + 1]:
                last_swap = j + 1
                array[j], array[j + 1] = array[j + 1], array[j]
        size = last_swap

    return array


if __name__ == '__main__':
    array = [5, 1, 45, 100, 4, 46, 78, 22, 11]
    array1 = [1, 2, 3, 4, 5, 6]
    array2 = [2, 1, 3, 4, 5, 6]
    # print(bubble_sort(array))
    print(bubble_sort_optimized(array2))
    # print(bubble_sort_optimized(array))
