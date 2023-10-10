from heapq import heapify
from random import randint


def heapify_max(array: list, index: int, heap_size: int):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    if left < heap_size and array[largest] < array[left]:
        largest = left
    if right < heap_size and array[largest] < array[right]:
        largest = right
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        heapify_max(array, largest, heap_size)


def build_maxheap(array: list):
    size = len(array)
    for i in range(size // 2, -1, -1):
        heapify_max(array, i, len(array))


def heap_sort(array: list):
    build_maxheap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify_max(array, 0, i)
    return array


if __name__ == '__main__':
    def stress_test():
        for _ in range(100_000):
            n = randint(1, 15)
            seq = [randint(-30, 30) for i in range(n)]
            print(seq)
            seq2 = seq.copy()
            heapify(seq)
            build_maxheap(seq2)
            if seq != seq2:
                print("WA")
                break


    # array = [5, 1, 45, 100, 4, 46, 78, 22, 11]
    # array = [22, -13, -2, 1, 8, 24, -25, -10]
    # print(heap_sort(array))
    # stress_test()
    seq = [18, 0, -10, 14, 17, -24, -6, -16, 8, -9, -3, 7]
    seq2 = [18, 0, -10, 14, 17, -24, -6, -16, 8, -9, -3, 7]
    build_maxheap(seq)
    heapify(seq2)
    print(seq)
    print(seq2)