import itertools


def choose_current_best(set_: set, sets: list[set], covered: set):
    uncovered = set_ - covered
    best_current = {}
    for item in sets:
        if len(uncovered & item) > len(best_current):
            best_current = item

    return best_current


# def unite(set_list: list[set]):
#     result = set()
#     for item in set_list:
#         result = result.union(item)
#     return result


def find_set_cover(set_: set, sets: list[set]) -> list[set]:
    covered = set()
    result = []
    for _ in range(len(sets)):
        current_best = choose_current_best(set_, sets, covered)
        sets.remove(current_best)
        result.append(current_best)
        covered = covered.union(current_best)
        if covered == set_:
            return result
    else:
        return []


def all_0_1_sequences(length: int) -> list[list[int]]:
    current = [[]]
    while len(current[0]) != length:
        next = []
        while current:
            a = current.pop()
            b = a.copy()
            a.append(0)
            b.append(1)
            next.append(a)
            next.append(b)

        current = next

    return current


def check_cover(set_: set, sets: list[set[int]]):
    cover = set()
    for item in sets:
        cover = cover.union(item)

    if cover == set_:
        return True


def slow_set_cover_bad_memory(set_: set, sets: list[set]) -> list[list[set[int]]]:
    sequences = all_0_1_sequences(len(sets))
    result = []
    min_len = len(sets)
    for sequence in sequences:
        set_list = []
        for i in range(len(sequence)):
            if sequence[i]:
                set_list.append(sets[i])

        if check_cover(set_, set_list):
            # result.append(set_list)
            if len(set_list) < min_len:
                result.clear()
                result.append(set_list)
                min_len = len(set_list)
            elif len(set_list) == min_len:
                result.append(set_list)
    return result


def slow_set_cover(set_: set, sets: list[set]) -> list[list[set[int]]]:
    sequences = itertools.product([0, 1], repeat=len(sets))
    result = []
    min_len = len(sets)
    for sequence in sequences:
        set_list = []
        for i in range(len(sequence)):
            if sequence[i]:
                set_list.append(sets[i])

        if check_cover(set_, set_list):
            # result.append(set_list)
            if len(set_list) < min_len:
                result.clear()
                result.append(set_list)
                min_len = len(set_list)
            elif len(set_list) == min_len:
                result.append(set_list)
    return result


if __name__ == '__main__':
    # set_ = set([1, 2, 3, 4, 5, 6, 7])
    # print(all_0_1_sequences(3))
    # print(check_cover(set([1,2,3]),[set([1,2]),set([2,3])]))
    print(slow_set_cover({1, 2, 3, 4, 5, 6}, [{1, 2}, {3, 4}, {1, 5, }, {2, 6}, {1, 2, 3, 4}]))
    print(find_set_cover({1, 2, 3, 4, 5, 6}, [{1, 2}, {3, 4}, {1, 5, }, {2, 6}, {1, 2, 3, 4}]))
