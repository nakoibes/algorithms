class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        """int to str, int to list"""
        if x < 0:
            return False
        number_list = []
        while x:
            number_list.append(x % 10)
            x //= 10

        half_size = len(number_list) // 2
        for i in range(half_size):
            if number_list[i] != number_list[-i - 1]:
                return False

        return True


class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        digit_number = 0
        while number:
            number //= 10
            digit_number += 1
        for i in range(1, digit_number // 2 + 1):
            y = x // 10 ** (i - 1)
            y %= 10
            z = x // 10 ** (digit_number - i)
            z %= 10
            if y != z:
                return False
        return True


class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        _reversed = 0
        number = x
        while number > _reversed:
            _reversed = number % 10 + _reversed * 10
            number //= 10
        if _reversed == number or _reversed // 10 == number:
            return True
        return False


class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()

    print(s.isPalindrome(1))
    print(s.isPalindrome(10))
    print(s.isPalindrome(121))
    print(s.isPalindrome(15555551))
    print(s.isPalindrome(123321))
    print("________")
    print(s.isPalindrome(12))
    print(s.isPalindrome(1234431))
