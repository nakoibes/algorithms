from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max1 = 0
        zeroflag = False
        current_counter = 0
        prev1 = False
        previous_counter = 0
        for num in nums:
            if num == 0:
                zeroflag = True
                if prev1:
                    if previous_counter and max1 < previous_counter + current_counter:
                        max1 = previous_counter + current_counter
                    elif current_counter > max1:
                        max1 = current_counter
                    previous_counter = current_counter
                    current_counter = 0
                else:
                    previous_counter = 0
            else:
                prev1 = True
                current_counter += 1

        if prev1:
            if previous_counter and max1 < previous_counter + current_counter:
                max1 = previous_counter + current_counter
            elif current_counter > max1:
                max1 = current_counter

        if not zeroflag:
            return max1 - 1
        else:
            return max1


class Solution1:
    def longestSubarray(self, nums: List[int]) -> int:
        previous = 0
        current = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_len = max(max_len, current + previous)
                previous = current
                current = 0
            else:
                current += 1

        max_len = max(max_len, current + previous)
        if max_len == len(nums):
            return max_len-1
        return max_len



class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        last_zero = 0
        zero_counter = 0
        longest = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counter += 1
            if zero_counter > 1:
                longest = max(longest, i - start)
                start = last_zero + 1
                zero_counter = 1
            if nums[i] == 0:
                last_zero = i
        longest = max(longest, i - start + 1)

        return longest - 1


if __name__ == '__main__':
    s = Solution1()
    # print(s.longestSubarray([0, 0, 1, 0, 1, 1, 0, 1, 1, 1]))
    print(s.longestSubarray([1,1,0,1]))
