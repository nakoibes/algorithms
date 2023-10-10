from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """time - n, memo - 1"""
        first_1 = 0
        last_1 = len(seats) - 1
        while seats[first_1] != 1:
            first_1 += 1

        while seats[last_1] != 1:
            last_1 -= 1

        max_gap = 0
        current_last = first_1
        for i in range(first_1 + 1, last_1 + 1):
            seat = seats[i]
            if seat == 1:
                if i - current_last > max_gap:
                    max_gap = i - current_last
                current_last = i

        return max(first_1, len(seats) - 1 - last_1, max_gap // 2)


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = [len(seats)] * len(seats)
        right = [len(seats)] * len(seats)
        max_gap = 0
        for i in range(0, len(seats)):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < len(seats) - 1:
                right[i] = right[i + 1] + 1

        for i in range(len(seats)):
            if min(left[i], right[i]) > max_gap:
                max_gap = min(left[i], right[i])

        return max_gap


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2)
    print(s.maxDistToClosest([1, 0, 0, 0]) == 3)
    print(s.maxDistToClosest([0, 1]) == 1)
