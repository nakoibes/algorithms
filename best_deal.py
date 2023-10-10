"""given: array of prices; best days to sell and purchase to be found"""


def find_best_deal(array: list[int]) -> tuple[int, int]:
    """time: n^2; auxiliary memory: 1"""
    size = len(array)
    best_difference = 0
    best_deal = (0, 0)
    for i in range(size):
        for j in range(i + 1, size):
            difference = array[j] - array[i]
            if difference > best_difference:
                best_deal = (i, j)
                best_difference = difference
    return best_deal


def find_best_deal_faster(array: list[int]) -> tuple[int, int]:
    """time: n; auxiliary memory: n"""
    auxiliary: list[int] = list()
    auxiliary.append(0)
    size = len(array)
    for i in range(1, size):
        if array[i] < array[auxiliary[i - 1]]:
            auxiliary.append(i)
        else:
            auxiliary.append(auxiliary[i - 1])

    best_difference = 0
    best_deal = (0, 0)
    for i in range(1, size):
        difference = array[i] - array[auxiliary[i]]
        if difference > best_difference:
            best_difference = difference
            best_deal = (auxiliary[i], i)

    return best_deal


def find_max_index_in_slice(array: list, left: int, right: int):
    temp_max_index = left
    temp_max = array[left]
    for i in range(left + 1, right + 1):
        if array[i] > temp_max:
            temp_max = array[i]
            temp_max_index = i
    return temp_max_index


def find_min_index_in_slice(array: list, left: int, right: int):
    temp_min_index = left
    temp_min = array[left]
    for i in range(left + 1, right + 1):
        if array[i] < temp_min:
            temp_min = array[i]
            temp_min_index = i
    return temp_min_index


def find_best_deal_divide(array: list[int], left: int, right: int) -> tuple[int, int]:
    """time: n*log_n; auxiliary memory: 1"""
    size_ = right - left
    if size_ < 2:
        return left, right

    middle = (left + right) // 2

    best_left = find_best_deal_divide(array, left, middle)
    best_right = find_best_deal_divide(array, middle + 1, right)

    left_min_index = find_min_index_in_slice(array, left, middle)
    right_max_index = find_max_index_in_slice(array, middle + 1, right)

    left_difference = array[best_left[1]] - array[best_left[0]]
    right_difference = array[best_right[1]] - array[best_right[0]]
    middle_difference = array[right_max_index] - array[left_min_index]

    best_difference = max(left_difference, right_difference, middle_difference)

    if best_difference == right_difference:
        return best_right
    elif best_difference == left_difference:
        return best_left
    else:
        return left_min_index, right_max_index


def find_best_deal_optimized(array: list[int]) -> tuple[int, int]:
    """time: n; auxiliary memory: 1"""
    size = len(array)
    best_purchase_index = 0
    best_difference = 0
    best_deal = (0, 0)
    for i in range(1, size):
        difference = array[i] - array[best_purchase_index]
        if difference > best_difference:
            best_difference = difference
            best_deal = (best_purchase_index, i)
        if array[i] < array[best_purchase_index]:
            best_purchase_index = i
    return best_deal


if __name__ == '__main__':
    array = [27, 53, 7, 25, 33, 2, 32, 47, 43]
    # print(find_best_deal_divide(array, 0, len(array) - 1))
    print(find_best_deal_faster(array))
