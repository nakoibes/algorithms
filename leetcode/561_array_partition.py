from typing import List


class Solution:

    # def quick_sort_in_place(self, array: list, left, right):
    #     if right - left < 1:
    #         return array
    #     pivot_index = self.partition2(array, left, right)
    #     self.quick_sort_in_place(array, left, pivot_index - 1)
    #     self.quick_sort_in_place(array, pivot_index + 1, right)
    #     return array
    #
    # def partition2(self, array: list, left, right):
    #     pivot = array[left]
    #     i = left
    #     j = right + 1
    #     while True:
    #         while True:
    #             i += 1
    #             if array[i] > pivot or i == right:
    #                 break
    #
    #         while True:
    #             j -= 1
    #             if array[j] < pivot or j == left:
    #                 break
    #         if i >= j:
    #             array[left], array[j] = array[j], array[left]
    #             return j
    #
    #         array[i], array[j] = array[j], array[i]

    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum([1, 4, 3, 2]))
