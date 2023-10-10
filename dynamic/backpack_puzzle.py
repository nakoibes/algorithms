# # k = int(input())
# # items = []
# # for _ in range(k):
# #
# #     items.append(input().split())
# #
#
# items = [["player", 3000, 4], ['phone', 2000, 1], ["note", 2000, 3], ['gui', 1500, 1]]
# # items = [["abb", 7, 1], ["globe", 6, 1], ['gal', 9, 2], ['mus', 9, 4], ['paul', 8, 1]]
# # items = [["water", 10, 3], ["book", 3, 1], ['food', 9, 2], ['coat', 5, 2], ['cam', 6, 1]]
# max_weight = 4
#
# # max_weight = max(items, key=lambda item: item[2])[2]
#
# n = len(items)
# m = max_weight
#
# table = [[[0] for _ in range(m)] for _ in range(n)]
# num = 0
# for j in range(m):
#     if items[0][2] <= j + 1:
#         table[0][j][0] = items[0][1]
#         table[0][j].append(items[0][0])
#
# for i in range(1, n):
#     name, price, weight = items[i][0], items[i][1], items[i][2]
#     for j in range(m):
#         if j + 1 == weight and price > table[i - 1][j][0]:
#             table[i][j][0] = price
#             table[i][j].append(name)
#         elif j + 1 > weight and price + table[i - 1][j - weight][0] >= table[i - 1][j][0]:
#             table[i][j][0] = price + table[i - 1][j - weight][0]
#             table[i][j].extend(table[i - 1][j - weight][1:])
#             table[i][j].append(name)
#         else:
#             table[i][j] = table[i - 1][j]
# print(table[n - 1][m - 1])
from copy import copy
from functools import lru_cache, cache
import timeit


def solve_backpack(items: dict[int, tuple[int, int]], step, capacity):
    """В этом алгоритме нужно самому следить за разбиением таблицы"""

    # max_weight = max(items.values(), key=lambda x: x[1])[1]
    table_len = int(capacity // step)
    table = list()
    table.append([(0, set())] * table_len)
    table.append([(0, set())] * table_len)
    for i in range(table_len):
        current_capacity = (i + 1) * step
        price, weight = items[0]
        if weight <= current_capacity:
            table[0][i] = (price, {0})

    for item, characters in items.items():
        if item == 0:
            continue
        price, weight = characters
        for i in range(table_len):
            current_capacity = (i + 1) * step
            if weight > current_capacity:
                table[1][i] = table[0][i]
            else:
                previous_price = table[0][i][0]
                if step * (i + 1) - weight >= step:
                    current_price = price + table[0][int(((i + 1) * step - weight) // step) - 1][0]
                    # здесь мы считаем в какой ячейке находится цена с весом current_capacity - weight
                    current_set = table[0][int(((i + 1) * step - weight) // step) - 1][1].copy()
                    current_set.add(item)
                else:
                    current_price = price
                    current_set = {item}
                if current_price > previous_price:
                    table[1][i] = (current_price, current_set)
                else:
                    table[1][i] = (previous_price, table[0][i][1].copy())

        table[0] = table[1]
        table[1] = [(0, set())] * table_len

    return table[0][table_len - 1]


def solve_backpack_v2(items: dict[int, tuple[int, int]], capacity):
    # @lru_cache(None)
    @cache
    def best_price(last_number: int, capacity: int) -> tuple[int, set[int]]:
        if last_number == 0:
            if capacity >= items[0][1]:
                return items[0][0], {0, }.copy()
            return 0, set().copy()
        last_number_price = items[last_number][0]
        without_last_number = best_price(last_number - 1, capacity)
        if capacity - items[last_number][1] > 0:
            with_last_number = best_price(last_number - 1, capacity - items[last_number][1])
            if without_last_number[0] > with_last_number[0] + last_number_price:
                return copy(without_last_number)
            else:
                current_items = with_last_number[1].copy()
                current_items.add(last_number)
                return with_last_number[0] + last_number_price, current_items
        elif capacity - items[last_number][1] == 0:
            if without_last_number[0] > last_number_price:
                return copy(without_last_number)
            else:
                return last_number_price, {last_number, }.copy()
        else:
            return copy(without_last_number)

    res = best_price(len(items.keys()) - 1, capacity)
    print(best_price.cache_info())
    return res

# def lru_test(a):
#     return copy({1})

if __name__ == '__main__':
    items = {0: (1500, 1), 1: (3000, 4), 2: (2000, 3), 3: (2000, 1), 4: (1000, 1)}
    items1 = {0: (7, 0.5), 1: (6, 0.5), 2: (9, 1), 3: (9, 2), 4: (8, 0.5), }
    items2 = {0: (7, 1), 1: (6, 1), 2: (9, 1), 3: (9, 2), 4: (8, 2), }
    # items2 = {0: (7, 1), 1: (6, 1), 2: (9, 1),3: (9, 2)}
    items3 = {0: (10, 3), 1: (3, 1), 2: (9, 2), 3: (5, 2), 4: (6, 1)}
    # items3 = {0: (10, 3), 1: (3, 1), 2: (9, 2), 3: (6, 1)}
    items4 = {0: (10, 3), 1: (7, 1), 2: (8, 2)}
    # print(solve_backpack(items, 1, 4))
    # print(solve_backpack(items1, 0.5, 2))

    print(solve_backpack_v2(items4, 3))
    print(solve_backpack(items4, 1, 3))

    print(solve_backpack_v2(items, 4))
    print(solve_backpack(items, 1, 4))

    print(solve_backpack_v2(items3, 6))
    print(solve_backpack(items3, 1, 6))

    print(solve_backpack_v2(items1, 2))
    print(solve_backpack(items1, 0.5, 2))

    # print(solve_backpack_v2(items2, 4))
    # print(solve_backpack(items2, 1, 4))

    # b = lru_test(1)
    # b.add(2)
    # c = lru_test(1)
    # print(c)
