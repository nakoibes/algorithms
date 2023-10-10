class Solution(object):
    """time n^2, memory 1"""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution(object):
    """time n, memory n"""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            j = table.get(difference)
            if j is not None:
                return [i, j]
            else:
                table.update({nums[i]: i})


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
