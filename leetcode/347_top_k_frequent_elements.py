import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(sequence, left, right, key=lambda x: x):
            middle = (left + right) // 2
            sequence[middle], sequence[left] = sequence[left], sequence[middle]
            i = left
            j = right + 1
            pivot = key(sequence[left])
            while True:
                while True:
                    i += 1
                    if i >= right or key(sequence[i]) < pivot:
                        break
                while True:
                    j -= 1
                    if j <= left or key(sequence[j]) > pivot:
                        break
                if i < j:
                    sequence[i], sequence[j] = sequence[j], sequence[i]
                else:
                    sequence[j], sequence[left] = sequence[left], sequence[j]
                    return j

        nums_dict = dict()
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        nums_freq = list()
        for num, frequency in nums_dict.items():
            nums_freq.append((num, frequency))
        left = 0
        right = len(nums_freq) - 1
        index = partition(nums_freq, left, right, key=lambda x: x[1])

        while index != k - 1:
            if index < k - 1:
                left = index + 1
            else:
                right = index - 1

            index = partition(nums_freq, left, right, key=lambda x: x[1])
        ans = list()
        for i in range(k):
            ans.append(nums_freq[i][0])

        return ans


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = dict()
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        nums_freq = list()
        for num, frequency in nums_dict.items():
            nums_freq.append((num, frequency))

        nums_freq.sort(key=lambda x: x[1], reverse=True)

        ans = list()
        for i in range(k):
            ans.append(nums_freq[i][0])

        return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_counter = Counter(nums)

        nums_freq = list()
        for num, frequency in nums_counter.items():
            nums_freq.append((num, frequency))

        nums_freq.sort(key=lambda x: x[1], reverse=True)

        ans = list()
        for i in range(k):
            ans.append(nums_freq[i][0])

        return ans


from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))
    print(s.topKFrequent([2, 3, 4, 1, 4, 0, 4, -1, -2, -1], 2))
