from bisect import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        neighbours_left = list()
        neighbours_right = list()

        index = bisect(arr, x)

        i = index - 1
        j = index

        while i >= 0 or j < len(arr):

            if len(neighbours_left) + len(neighbours_right) == k:
                break

            left_difference = float("inf")
            right_difference = float("inf")
            if i >= 0:
                left_difference = x - arr[i]
            if j < len(arr):
                right_difference = arr[j] - x

            if left_difference <= right_difference:
                neighbours_left.append(arr[i])
                i -= 1
            else:
                neighbours_right.append(arr[j])
                j += 1
        neighbours_left.reverse()
        neighbours_left.extend(neighbours_right)
        return neighbours_left


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect(arr, x)

        i = index - 1
        j = index

        for _ in range(k):
            if i < 0:
                j += 1
            elif j >= len(arr):
                i -= 1
            else:
                if x - arr[i] <= arr[j] - x:
                    i -= 1
                else:
                    j += 1

        return arr[i+1:j]


if __name__ == '__main__':
    s = Solution()
    print(s.findClosestElements([1, 2, 3, 4, 5], 4, 3))
    print(s.findClosestElements([1, 2, 3, 4, 5], 4, -1))
