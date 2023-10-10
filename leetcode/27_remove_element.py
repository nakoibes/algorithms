from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        offset = 0
        # i = 0
        for i in range(len(nums)):
            nums[i - offset] = nums[i]
            if val == nums[i]:
                offset += 1

        return i - offset + 1


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        current_left = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[current_left], nums[i] = nums[i], nums[current_left]
                current_left += 1

        return current_left


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
