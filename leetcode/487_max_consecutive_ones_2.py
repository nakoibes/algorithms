from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_counter = 0
        last_zero = None
        left = 0
        right = 0
        max_len = 0
        while right < len(nums):
            if nums[right] == 0:
                if not last_zero:
                    last_zero = right

                zero_counter += 1
                if zero_counter > 1:
                    if right - left > max_len:
                        max_len = right - left
                    left = last_zero
                    zero_counter = 1
                last_zero = right
            right += 1

        if right - left > max_len:
            max_len = right - left

        return max_len


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        previous = 0
        current = 0
        max_sum = 0
        for num in nums:
            current += 1
            if num == 0:
                previous = current
                current = 0
            max_sum = max(max_sum, previous + current)

        # max_sum = max(max_sum, previous + current)

        return max_sum


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
    print(s.findMaxConsecutiveOnes([0, 0, 1, 1, 1]))
    print(s.findMaxConsecutiveOnes([1, 1, 1, 1, 1]))
    print(s.findMaxConsecutiveOnes([0]))
    print(s.findMaxConsecutiveOnes([1]))
    print(s.findMaxConsecutiveOnes([0, 1]))
    print(s.findMaxConsecutiveOnes([1, 0]))
