def selection_sort(array: list):
    size = len(array)
    for i in range(size - 1, -1, -1):
        index_max = 0
        for j in range(0, i+1):
            if array[j] > array[index_max]:
                index_max = j
        array[i], array[index_max] = array[index_max], array[i]
    return array


if __name__ == '__main__':
    array = [5, 1, 45, 100, 4, 46, 78, 22, 11]
    a = [1]
    print(selection_sort(array))
    print(selection_sort(a))
