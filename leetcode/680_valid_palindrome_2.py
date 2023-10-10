class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        right = len(s) - 1
        left = 0
        while left < right:
            if s[left] != s[right]:
                return check_palindrome(left, right - 1) or check_palindrome(left + 1, right)
            left += 1
            right -= 1

        return True



