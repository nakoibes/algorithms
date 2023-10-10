import timeit
from random import randint


def sign(number: int):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def find_longest_monotonous(sequence: list):
    if len(sequence) == 1:
        return 0, 0
    previous_status = sign(sequence[1] - sequence[0])
    best_start = 0
    best_finish = 0
    start = 0
    max_len = 0
    for i in range(1, len(sequence) - 1):
        if previous_status == 0:
            previous_status = sign(sequence[i + 1] - sequence[i])
            start = i
            continue
        current_status = sign(sequence[i + 1] - sequence[i])
        if current_status == 0:
            current_len = i - start + 1
            if current_len > max_len:
                max_len = current_len
                best_start = start
                best_finish = i
            start = i + 1
        elif previous_status != current_status:
            current_len = i - start + 1
            if current_len > max_len:
                max_len = current_len
                best_start = start
                best_finish = i
            start = i

        previous_status = current_status

    if len(sequence) - start > max_len and previous_status != 0:
        best_start = start
        best_finish = len(sequence) - 1

    return best_start, best_finish


def find_longest_ascending(sequence: list):
    best_start = 0
    best_finish = 0
    start = 0
    finish = 0
    max_len = 0
    for i in range(len(sequence) - 1):
        if sequence[i + 1] <= sequence[i]:
            if finish - start > max_len:
                best_start = start
                best_finish = finish
                max_len = finish - start
            start = i + 1
            finish = i + 1
        else:
            finish = i + 1

    if finish - start > max_len:
        best_start = start
        best_finish = finish

    return best_start, best_finish


def find_longest_descending(sequence: list):
    best_start = 0
    best_finish = 0
    start = 0
    finish = 0
    max_len = 0
    for i in range(len(sequence) - 1):
        if sequence[i + 1] >= sequence[i]:
            if finish - start > max_len:
                best_start = start
                best_finish = finish
                max_len = finish - start
            start = i + 1
            finish = i + 1
        else:
            finish = i + 1

    if finish - start > max_len:
        best_start = start
        best_finish = finish

    return best_start, best_finish


def find_status(num1, num2):
    if num2 > num1:
        return 1
    elif num2 < num1:
        return -1
    else:
        return 0


# def find_longest_monotonous_1(nums: list):
#     if len(nums) == 1:
#         return 1
#     max_len = 0
#     left = 0
#     previous_status = find_status(nums[0], nums[1])
#     for i in range(1, len(nums) - 1):
#         current_status = find_status(nums[i], nums[i + 1])
#         if previous_status == 0:
#             previous_status = current_status
#             left = i
#             continue
#         elif current_status == 0:
#             max_len = max(max_len, i - left + 1)
#             left = i + 1
#         elif previous_status != current_status:
#             max_len = max(max_len, i - left + 1)
#             left = i
#
#         previous_status = current_status
#
#     if previous_status == 0:
#         max_len = max(1, max_len)
#     else:
#         max_len = max(max_len, len(nums) - left)
#
#     return max_len
def find_longest_monotonous_1(nums: list):
    if len(nums) == 1:
        return 0, 0
    max_len = 0
    best_left = 0
    best_right = 0
    left = 0
    previous_status = find_status(nums[0], nums[1])
    if previous_status != 0:
        right = 1
    else:
        right = 0
    for i in range(1, len(nums) - 1):

        current_status = find_status(nums[i], nums[i + 1])
        if previous_status == 0:
            previous_status = current_status
            left = i
            right = i
            continue
        elif current_status == 0:
            right = i
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                best_left = left
                best_right = right
            # max_len = max(max_len, i - left + 1)
            left = i + 1
        elif previous_status != current_status:
            # max_len = max(max_len, i - left + 1)
            right = i
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                best_left = left
                best_right = right
            left = i

        previous_status = current_status

    if previous_status != 0:
        right = len(nums) - 1
        current_len = right - left + 1
    else:
        right = left
        current_len = 1
    if current_len > max_len:
        best_left = left
        best_right = right

    return best_left, best_right


def find_longest_monotonous_2(sequence: list):
    left_asc = 0
    left_desc = 0
    longest_asc = 0
    longest_desc = 0
    best_left_acs = 0
    best_left_desc = 0
    best_right_acs = 0
    best_right_desc = 0
    for i in range(len(sequence) - 1):
        if sequence[i + 1] > sequence[i]:
            if i + 1 - left_asc + 1 > longest_asc:
                longest_asc = i + 1 - left_asc + 1
                best_left_acs = left_asc
                best_right_acs = i + 1
            left_desc = i + 1
        elif sequence[i + 1] < sequence[i]:
            if i + 1 - left_desc + 1 > longest_desc:
                longest_desc = i + 1 - left_desc + 1
                best_left_desc = left_desc
                best_right_desc = i + 1
            left_asc = i + 1
        else:
            left_asc = i + 1
            left_desc = i + 1

    if longest_asc > longest_desc:
        return best_left_acs, best_right_acs
    else:
        return best_left_desc, best_right_desc


if __name__ == '__main__':
    def stress_test_1():
        for _ in range(100_000):
            n = randint(1, 20)
            seq = [randint(-20, 20) for _ in range(n)]
            print(seq)
            l1 = find_longest_monotonous(seq)
            l2 = find_longest_monotonous_1(seq)
            if l1[1] - l1[0] != l2[1] - l2[0]:
                print("WA")
                break

    def stress_test_2():
        timer1 = 0
        timer2 = 0
        for _ in range(100_000):
            n = randint(1, 10)
            seq = [randint(-20, 20) for _ in range(n)]
            # print(seq)
            start = timeit.default_timer()
            l1 = find_longest_monotonous(seq)
            timer1 += (timeit.default_timer()-start)
            start = timeit.default_timer()
            l2 = find_longest_monotonous_2(seq)
            timer2 += (timeit.default_timer()-start)
            if l1[1] - l1[0] != l2[1] - l2[0]:
                print("WA")
                break
        print("difficult:", timer1)
        print("easy:", timer2)

    def stress_test():
        timer1 = 0
        timer2 = 0
        for _ in range(1000_000):
            n = randint(20, 100)
            seq = [randint(-20, 20) for _ in range(n)]
            start = timeit.default_timer()
            b_s_a, b_f_a = find_longest_ascending(seq)
            b_s_d, b_f_d = find_longest_descending(seq)
            if b_f_a - b_s_a > b_f_d - b_s_d:
                best_start = b_s_a
                best_finish = b_f_a
            else:
                best_start = b_s_d
                best_finish = b_f_d
            timer1 += (timeit.default_timer() - start)
            start = timeit.default_timer()
            f_m = find_longest_monotonous(seq)
            timer2 += (timeit.default_timer() - start)
            if (best_finish - best_start) != (f_m[1] - f_m[0]):
                print("WA")
                break
        print("asc+desc:", timer1)
        print("1 passage:", timer2)


    # print(find_longest_monotonous([1, 2, 3]) == (0, 2))
    # print(find_longest_monotonous([1]) == (0, 0))
    # print(find_longest_monotonous([1, 2]) == (0, 1))
    # print(find_longest_monotonous([1, 2, 1, 4, 7, 9, 1]) == (2, 5))
    # print(find_longest_monotonous([1, 2, 1, 2, 3, 1, 2, 3, 4]) == (5, 8))
    # print(find_longest_monotonous([1, 1]) == (0, 0))
    # print(find_longest_monotonous([1, 10, 10, 1, 2, 3]) == (3, 5))
    # print(find_longest([1, 1, 1, 10, 10, 1, 2, 3]) == (3, 5))
    # print(find_longest_monotonous([1, 1, 1, 2, 3, 4, 4, 4, 3, 2, 1, 0]) == (7, 11))
    # print(find_longest_monotonous([1, 2, 3, 4, 5, 4, 4, 4, 3, 2, 1, 0]) == (0, 4))
    # print(find_longest_monotonous([1, 1, 1, 2, 3, 4, 4, 4, 3, 2, 1, 0]))
    # print(find_longest_monotonous([1, 1, 1]))
    # print(find_longest_monotonous([6, -5, -4, 10, 2, 13, -10, -1, -11, 13, -18, 15]))
    stress_test_2()
    # print(find_longest_monotonous_1([-5, -5, -19, -19]))
    # print(find_longest_monotonous_2([6, -12, -20]))
