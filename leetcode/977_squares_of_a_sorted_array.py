from bisect import bisect
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list = list()
        i = 0
        j = len(nums) - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                square_list.append(nums[i] ** 2)
                i += 1
            else:
                square_list.append(nums[j] ** 2)
                j -= 1

        # square_list.append(nums[i] **2)
        square_list.reverse()
        return square_list


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                square_list[j - i] = nums[i] ** 2
                i += 1
            else:
                square_list[j - i] = nums[j] ** 2
                j -= 1
        return square_list


# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#
#         square_list = list()
#         index = bisect(nums, 0)
#         left = index - 1
#         right = index
#         for _ in range(len(nums)):
#             if right > len(nums) - 1 or abs(nums[left]) < abs(nums[right]):
#                 square_list.append(nums[left] ** 2)
#                 left -= 1
#             elif left < 0 or abs(nums[left]) >= abs(nums[right]):
#                 square_list.append(nums[right] ** 2)
#                 right += 1
#
#         return square_list


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
