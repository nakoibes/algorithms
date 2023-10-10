class Solution:
    "n^2 doesnt pass time limit"

    def shortestPalindrome(self, s: str) -> str:
        s = s[::-1]
        for start in range(len(s)):
            i = start
            j = len(s) - 1
            while i < len(s) and s[i] == s[j] and i <= j:
                i += 1
                j -= 1
            if i > j:
                return s + s[:start][::-1]
        return ""

# wrong
# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         s = s[::-1]
#         left = -1
#         right = len(s)
#         while True:
#             if left == right - 2 or left == right - 1:
#                 left_numbers = left + 1
#                 right_numbers = len(s) - right
#                 break
#             if s[left + 1] != s[right - 1]:
#                 left += 1
#                 right = len(s)
#             else:
#                 left += 1
#                 right -= 1
#
#         return s + s[:left_numbers - right_numbers][::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPalindrome("aacecaaa"))
