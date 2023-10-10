from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        max_height = height[0]
        right_max_index = 0
        for i in range(1, len(height)):
            if height[i] >= max_height:
                max_height = height[i]
                right_max_index = i
        left_wall_index = 0

        for i in range(1, right_max_index):
            if height[i] < height[left_wall_index]:
                result += height[left_wall_index] - height[i]
            else:
                left_wall_index = i
        right_wall = height[len(height) - 1]

        for j in range(len(height) - 2, right_max_index, -1):
            if height[j] < right_wall:
                result += right_wall - height[j]
            else:
                right_wall = height[j]

        return result



class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        size = len(height)
        if size <= 2:
            return 0
        left_max = 0
        right_max = size - 1
        left = 1
        right = size - 2
        while left <= right:
            if height[left_max] < height[right_max]:
                if height[left] < height[left_max]:
                    result += height[left_max] - height[left]
                else:
                    left_max = left
                left += 1
            else:
                if height[right] < height[right_max]:
                    result += height[right_max] - height[right]
                else:
                    right_max = right

                right -= 1

        return result