from random import randint
import timeit


def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def quick_sort(array: list):
    size = len(array)
    if size <= 1:
        return array
    pivot = array[0]
    less = []
    more = []
    for i in range(1, size):
        if array[i] < pivot:
            less.append(array[i])
        else:
            more.append(array[i])
    return quick_sort(less) + [pivot] + quick_sort(more)


def quick_sort_in_place(array: list, left, right):
    if right - left < 1:
        return array
    pivot_index = partition3(array, left, right)
    quick_sort_in_place(array, left, pivot_index - 1)
    quick_sort_in_place(array, pivot_index + 1, right)
    return array


def partition(array, left, right):
    middle = (left + right) // 2
    array[middle], array[right] = array[right], array[middle]
    pivot = array[right]
    future_pivot = left - 1
    for i in range(left, right):
        if array[i] < pivot:
            future_pivot += 1
            array[i], array[future_pivot] = array[future_pivot], array[i]
    future_pivot += 1
    array[future_pivot], array[right] = array[right], array[future_pivot]
    return future_pivot


def partition1(array: list, left, right):  # Проблема когда 2 значения пивот
    pivot_index = (left + right) // 2
    pivot = array[pivot_index]
    # left -= 1
    # right += 1
    while True:
        # left += 1
        while array[left] < pivot: left += 1
        # while True:
        #     left += 1
        #     if array[left] > pivot:
        #         break

        # while True:
        #     right -= 1
        #     if array[right] < pivot:
        #         break
        # right -= 1
        while array[right] > pivot: right -= 1
        if left >= right or (array[left] == pivot and array[right] == pivot):
            return right
        array[left], array[right] = array[right], array[left]
        # left += 1
        # right -= 1


def partition2(array: list, left: int, right: int):
    pivot = array[left]
    i = left
    j = right + 1
    while True:
        while True:
            i += 1
            if array[i] > pivot or i == right:
                break

        while True:
            j -= 1
            if array[j] < pivot or j == left:
                break
        if i >= j:
            array[left], array[j] = array[j], array[left]
            return j

        array[i], array[j] = array[j], array[i]


def partition3(sequence: list, left: int, right: int):
    pivot = sequence[(left + right) // 2]
    equal_first = left
    greater_first = left
    for i in range(left, right + 1):
        if sequence[i] == pivot:
            sequence[i], sequence[greater_first] = sequence[greater_first], sequence[i]
            greater_first += 1
        elif sequence[i] < pivot:
            tmp = sequence[i]
            sequence[i] = sequence[greater_first]
            sequence[greater_first] = sequence[equal_first]
            sequence[equal_first] = tmp
            equal_first += 1
            greater_first += 1

    return equal_first


def kth_value(sequence: list, k: int):  # Оно точно за линию работает?(k*n)
    left = 0
    right = len(sequence) - 1
    while left < right:
        index = partition3(sequence, left, right)
        if index + 1 > k:
            right = index - 1
        elif index + 1 < k:
            left = index + 1
        else:
            return


def test_partition() -> bool:
    for i in range(10_000):
        n = randint(2, 100)
        sequence = [randint(-1000, 1000) for _ in range(n)]
        # print(sequence)
        res = partition(sequence, 0, len(sequence) - 1)
        for j in range(res):
            if sequence[j] > sequence[res]:
                return False

        for j in range(res + 1, len(sequence)):
            if sequence[j] < sequence[res]:
                return False

    return True


def quick_sort_left_part():
    pass


if __name__ == '__main__':
    # a = [50, 3, 3, 34, 544, 544, 100, 45, 45, 888, 1000, 32, 8, 8]
    # b = [-22, -23, 40, 33, 10, -33, 23, 19]
    # print(partition(a, 0, len(a) - 1))
    # print(quicksort(a))
    # print(quick_sort_in_place(a, 0, len(a) - 1))
    # print(quick_sort_in_place(b, 0, len(b) - 1))

    # b = [6, 6, 6, 2, 3, 10, 7, 8, 1]

    # print(partition2(b, 0, len(b) - 1))
    # print(b)

    def stress_test():
        for i in range(10000):

            n = randint(1, 20)
            a = [randint(-50, 50) for _ in range(n)]
            # print(a)
            b = a.copy()
            quick_sort_in_place(a, 0, len(a) - 1)
            b.sort()
            if a != b:
                # print(i)
                # print(a)
                # print(b)
                break


    # # c = [1, 5, 7, 8, 8, 8, 45, 34, 32, 21]
    # # print(partition(c, 0, len(c) - 1))
    # seq = [4, 120, 60, 4, 100, 100, 600, 6, 300]
    # # partition3(seq, 0, len(seq) - 1)
    # kth_value(seq, 1)
    # kth_value(seq, 2)
    # kth_value(seq, 2)
    # kth_value(seq, len(seq))
    # kth_value(seq, len(seq) - 1)
    # print(seq[0])
    # print(seq[1])
    # print(seq[len(seq) - 1])
    # print(seq[len(seq) - 2])
    #
    # d = 1
    #
    # # stress_test()

    # seq1 = [randint(-1000, 1000) for _ in range(100_000)]
    # seq2 = [randint(-1000, 1000) for _ in range(200_000)]

    # st1 = timeit.default_timer()
    # seq1.sort()
    # print(timeit.default_timer() - st1)
    #
    # st2 = timeit.default_timer()
    # seq2.sort()
    # print(timeit.default_timer() - st2)

    # st1 = timeit.default_timer()
    # quick_sort_in_place(seq1, 0, len(seq1)-1)
    # print(timeit.default_timer() - st1)
    #
    # st2 = timeit.default_timer()
    # quick_sort_in_place(seq2, 0, len(seq2)-1)
    # print(timeit.default_timer() - st2)


