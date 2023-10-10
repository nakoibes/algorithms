import itertools
from bisect import bisect, bisect_left
from functools import cache
from typing import List


def check_increase(numbers: list):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """time - 2^n; space - n"""
        prod = itertools.product([0, 1], repeat=len(nums))
        max_len = 0
        for item in prod:
            subsequence = list()
            for i in range(len(item)):
                if item[i]:
                    subsequence.append(nums[i])

            if len(subsequence) > max_len and check_increase(subsequence):
                max_len = len(subsequence)

        return max_len


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """time 2^n, space n"""

        def find_longest(last_i, i):
            if i == len(nums):
                return 0
            take = 0
            dont_take = find_longest(last_i, i + 1)

            if last_i is None or nums[last_i] < nums[i]:
                take = find_longest(i, i + 1) + 1
            return max(take, dont_take)

        return find_longest(None, 0)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """time n^2, space - n^2"""

        @cache
        def find_longest(last_i, i):
            if i == len(nums):
                return 0
            take = 0
            dont_take = find_longest(last_i, i + 1)

            if last_i is None or nums[last_i] < nums[i]:
                take = find_longest(i, i + 1) + 1
            return max(take, dont_take)

        res = find_longest(None, 0)
        print(find_longest.cache_info())
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """time - n^2; space - n"""
        dp = [-1] * (len(nums) + 1)

        def find_longest(last_i, i):
            if dp[last_i] != -1:
                return dp[last_i]
            if i == len(nums):
                return 0
            take = 0
            dont_take = find_longest(last_i, i + 1)

            if last_i == -1 or nums[last_i] < nums[i]:
                take = find_longest(i, i + 1) + 1

            dp[last_i] = max(take, dont_take)
            return max(take, dont_take)

        res = find_longest(-1, 0)
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """time - n^2; space - n"""
        dp = [1] * (len(nums))
        max_len = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(max_len, dp[i])

        return max_len


class Solution:

    def find_index(self, sequence, value):
        if sequence[0] >= value:
            return -1
        for i in range(len(sequence) - 1):
            if sequence[i + 1] >= value:
                return i

    def lengthOfLIS(self, nums: List[int]) -> int:
        """time n^3?; space - n^2?"""
        sequences = list()
        sequences.append([nums[0]])
        for i in range(1, len(nums)):
            current = nums[i]
            append_flag = False
            for j in range(len(sequences)):
                sequence = sequences[j]
                if current > sequence[-1]:
                    sequence.append(current)
                    append_flag = True
                else:
                    k = self.find_index(sequence, current)
                    if k != -1:
                        new_sequence = sequence[:k + 1]
                        new_sequence.append(current)
                        if new_sequence not in sequences:
                            sequences.append(new_sequence)
            if not append_flag:
                sequences.append([current])

        return len(max(sequences, key=len))


class Solution:
    def find_first_greater_eq(self, sequence, value):
        left = 0
        right = len(sequence) - 1
        while left < right:
            middle = (left + right) // 2
            if sequence[middle] == value:
                return middle
            if sequence[middle] > value:
                right = middle
            else:
                left = middle + 1

        return right

    def lengthOfLIS(self, nums: List[int]) -> int:
        """time - n logn; space - n"""
        sequence = [nums[0]]
        for i in range(1, len(nums)):
            current = nums[i]
            if current > sequence[-1]:
                sequence.append(current)
            elif current < sequence[-1]:
                # j = self.find_first_greater_eq(sequence, current)
                j = bisect_left(sequence, current)
                sequence[j] = current

        return len(sequence)


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        """time - n logn; space - 1"""
        length = 1
        for i in range(1, len(nums)):
            current = nums[i]
            if current > nums[length - 1]:
                nums[length] = current
                length += 1
            elif current < nums[length - 1]:
                j = bisect_left(nums, current, lo=0, hi=length)
                nums[j] = current

        return length

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        """time - n logn; space - 1"""
        length = 1
        for i in range(1, len(nums)):
            current = nums[i]
            if current > nums[length - 1]:
                nums[length] = current
                length += 1
            elif current < nums[length - 1]:
                j = bisect_left(nums, current, lo=0, hi=length)
                nums[j] = current

        return length


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    # print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
    # print(s.lengthOfLIS(
    #     [-813, 82, -728, -82, -432, 887, -551, 324, -315, 306, -164, -499, -873, -613, 932, 177, 61, 52, 1000, -710,
    #      372, -306, -584, -332, -500, 407, 399, -648, 290, -866, 222, 562, 993, -338, -590, 303, -16, -134, 226, -648,
    #      909, 582, 177, 899, -343, 55, 629, 248, 333, 1, -921, 143, 629, 981, -435, 681, 844, 349, 613, 457, 797, 695,
    #      485, 15, 710, -450, -775, 961, -445, -905, 466, 942, 995, -289, -397, 434, -14, 34, -903, 314, 862, -441, 507,
    #      -966, 525, 624, -706, 39, 152, 536, 874, -364, 747, -35, 446, -608, -554, -411, 987, -354, -700, -34, 395,
    #      -977, 544, -330, 596, 335, -612, 28, 586, 228, -664, -841, -999, -100, -620, 718, 489, 346, 450, 772, 941, 952,
    #      -560, 58, 999, -879, 396, -101, 897, -1000, -566, -296, -555, 938, 941, 475, -260, -52, 193, 379, 866, 226,
    #      -611, -177, 507, 910, -594, -856, 156, 71, -946, -660, -716, -295, -927, 148, 620, 201, 706, 570, -659, 174,
    #      637, -293, 736, -735, 377, -687, -962, 768, 430, 576, 160, 577, -329, 175, 51, 699, -113, 950, -364, 383, 5,
    #      748, -250, -644, -576, -227, 603, 832, -483, -237, 235, 893, -336, 452, -526, 372, -418, 356, 325, -180, 134,
    #      -698]))

    # a = [0, 1]
    # print(bisect_left(a, 0))
    # i = 1
    # print(all(val < 0 for val in a[0: i]))
