def _expand_dict(item, path, result: list):
    if isinstance(item, dict):
        for key, value in item.items():
            _expand_dict(value, path + [key], result)
    else:
        result.append((item, path))


def expand_dict(input_dict: dict):
    result = list()
    path = []
    _expand_dict(input_dict, path, result)
    return result


if __name__ == '__main__':
    print(expand_dict({1: {2: 3, 4: 5}, 4: {2: {6: 2, 7: 1}, 8: 10}}))
