class Solution:
    def isPalindrome(self, s: str) -> bool:
        """time - n; space - n"""

        s = s.translate({ord("."): None, ord("!"): None, ord("#"): None, ord(")"): None, ord("("): None, ord("*"): None,
                         ord("&"): None, ord("$"): None, ord("^"): None, ord("%"): None, ord("@"): None, ord(","): None,
                         ord(":"): None, ord(";"): None, ord("-"): None, ord("_"): None,
                         ord(" "): None, ord("/"): None, ord("}"): None, ord("{"): None, ord("["): None, ord("]"): None,
                         ord("'"): None, ord("\""): None, ord("?"): None, ord("`"): None, })
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """time - n; space - 1"""
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
