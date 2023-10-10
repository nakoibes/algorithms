from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """time - n+m; space - m+n"""
        dict_1 = dict()
        dict_2 = dict()
        result = []
        for number in nums1:
            dict_1[number] = dict_1.get(number, 0) + 1
        for number in nums2:
            dict_2[number] = dict_2.get(number, 0) + 1

        for number, frequency in dict_1.items():
            if number in dict_2:
                for i in range(min(frequency, dict_2[number])):
                    result.append(number)

        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """time - n+m; space - n"""
        dict_1 = dict()
        # dict_2 = dict()
        result = []
        for number in nums1:
            dict_1[number] = dict_1.get(number, 0) + 1

        for number in nums2:
            if number in dict_1 and dict_1[number] != 0:
                result.append(number)
                dict_1[number] -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
