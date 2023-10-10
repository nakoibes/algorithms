import timeit
from random import randint
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                if counter > max_count:
                    max_count = counter
                counter = 0

        if counter > max_count:
            max_count = counter

        return max_count


class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        counter = 0
        for num in nums:
            if num == 0:
                longest = max(longest, counter)
                counter = 0
            else:
                counter += 1

        longest = max(longest, counter)
        return longest


if __name__ == '__main__':
    def time_test():
        timer = 0
        timer1 = 0
        for _ in range(100_000):
            n = randint(20, 100)
            seq = [randint(0, 1) for _ in range(n)]
            s = Solution()
            s1 = Solution1()
            st = timeit.default_timer()
            s.findMaxConsecutiveOnes(seq)
            timer += (timeit.default_timer() - st)
            st = timeit.default_timer()
            s1.findMaxConsecutiveOnes(seq)
            timer1 += (timeit.default_timer() - st)

        print("no max:", timer)
        print("with max:", timer1)


    # s = Solution()
    # print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    time_test()