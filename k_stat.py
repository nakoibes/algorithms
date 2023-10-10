from sorts.quicksort import partition2, quick_sort_in_place


def find_k_stat(sequence: list, k: int) -> int:
    left = 0
    right = len(sequence) - 1
    # middle = (left + right) // 2
    index = partition2(sequence, left, right)
    right_len = len(sequence) - index - 1
    while right_len != k:
        if right_len < k:
            right = index - 1
            index = partition2(sequence, left, right)
            right_len = len(sequence) - index - 1
        else:
            left = index + 1
            index = partition2(sequence, index + 1, right)
            right_len = len(sequence) - index - 1
    quick_sort_in_place(sequence, index + 1, len(sequence) - 1)
    return sequence[-k]


if __name__ == '__main__':
    # sequence = [4, 54, 32, 7, 22, 3, 55]
    # find_k_stat(sequence, 3)

    def test(sequence: list, k):

        res = find_k_stat(sequence, k)
        sequence.sort()
        res2 = sequence[len(sequence) - k]
        if res != res2:
            print(res, res2)
            return False
        return True


    from random import randint

    for _ in range(100):
        n = randint(5, 5)
        l = [randint(-100, 100) for i in range(n)]
        # print(l)
        if not test(l, 3):
            break

    print(find_k_stat([0, 0, 1, 2, 3], 3))

    # test([74, -67, -72, -83, -2], 3)
