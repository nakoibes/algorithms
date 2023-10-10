from copy import deepcopy
from typing import Iterable


def create_power_set(items: Iterable) -> list[list]:
    power_set = list()
    power_set.append(list())
    for item in items:
        new_sets = deepcopy(power_set)
        for set_ in new_sets:
            set_.append(item)
        power_set.extend(new_sets)

    return power_set

if __name__ == '__main__':
    items = [1, 2, 3, 4]
    print(create_power_set(items))
