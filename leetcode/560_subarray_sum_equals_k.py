from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        counter = 0
        current_sum = nums[0]
        while right < len(nums) - 1:
            if current_sum == k:
                counter += 1
                # current_sum -= nums[left]
                current_sum += nums[right + 1]
                # left += 1
                right += 1
            elif current_sum > k and left < right:
                current_sum -= nums[left]
                left += 1
            else:
                current_sum += nums[right + 1]
                right += 1

        # while True:

        if current_sum == k:
            counter += 1

        while left < right:
            current_sum -= nums[left]
            if current_sum == k:
                counter += 1
                break
            left += 1

        return counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """time - n^2; space - 1; timelimit"""
        counter = 0
        for i in range(len(nums)):
            current_sum = nums[i]
            if current_sum == k:
                counter += 1
            for j in range(i + 1, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    counter += 1

        return counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """time - n; space - n"""
        result = 0
        prefix_sum = 0
        d = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in d:
                result += d[prefix_sum - k]

            d[prefix_sum] = d.get(prefix_sum, 0) + 1

        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.subarraySum([1, 1, 1], 2))
    print(s.subarraySum([1, 2, 3], 3))
    print(s.subarraySum([1, -1, 0], 0))
