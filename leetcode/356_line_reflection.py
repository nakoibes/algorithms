'''Premium problem'''


def compare_points(point1: tuple[int, int], point2: tuple[int, int]):
    if point1[0] > point2[0]:
        return point1
    elif point1[0] == point2[0]:
        if point1[1] > point2[1]:
            return point1
        else:
            return point2
    else:
        return point2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if self.x > other.x:
            return True
        else:
            if self.x >= 0:
                if self.y > other.y:
                    return True
                else:
                    return False
            else:
                if self.y < other.y:
                    return True
                else:
                    return False

    def __repr__(self):
        return f"({self.x}, {self.y})"


def check_line_v2(sequence: list):
    for i, point in enumerate(sequence):
        sequence[i] = Point(*point)
    sequence.sort()


def check_line(sequence: list):
    """time - n, memo - n"""
    point_set = set()
    min_x = float("inf")
    max_x = -float("inf")
    for x, y in sequence:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        point_set.add((x, y))
    line_coord = min_x + max_x
    return all((line_coord - x, y) in point_set for x, y in sequence)


if __name__ == '__main__':
    sequence = [[1, 1], [1, 2], [-1, 3], [-1, 0], [0, 0]]
    check_line_v2(sequence)
    print(sequence)
    # print(check_line([[1, 1], [-1, 1]]))
