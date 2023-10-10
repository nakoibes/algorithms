"""Дается массив nums длины n и дается число q. После делается q запросов, каждый - это 2 числа l,r: 0<=l<=r<n.
Вы должны прибавить к числам nums[l],...,nums[r] по единице, вывести полученный массив.
"""


def add_ones(nums: list, requests: list):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    for i, j in requests:
        nums[i] += 1
        if j < len(nums)-1:
            nums[j+1] -= 1

    new_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        new_sum[i] = new_sum[i - 1] + nums[i - 1]

    for i in range(1, len(new_sum)):
        nums[i - 1] = new_sum[i] - prefix_sum[i - 1]

    return nums


if __name__ == '__main__':
    print(add_ones([1, 2, 3, 4, 5, 6], [(2, 4), (4, 5)]))
