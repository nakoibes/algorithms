from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        parenthes = deque()
        parenthes.append(s[0])
        for i in range(1, len(s)):
            if len(parenthes) > 0:
                last_parenth = parenthes.pop()
                if last_parenth != pairs.get(s[i]):
                    parenthes.append(last_parenth)
                    parenthes.append(s[i])
            else:
                parenthes.append(s[i])

        if len(parenthes) == 0:
            return True
        return False


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")",
                 "[": "]",
                 "{": "}"}
        stack = deque()
        for i in range(len(s)):
            for symbol in s:
                if symbol in pairs:
                    stack.append(symbol)
                elif len(stack) == 0 or symbol != pairs[stack.pop()]:
                    return False

        return len(stack) == 0


class Solution:
    """WRONG APPROACH"""
    def isValid(self, s: str) -> bool:
        counter1 = 0
        counter2 = 0
        counter3 = 0
        for sym in s:
            if sym == "(":
                counter1 += 1
            elif sym == ")":
                counter1 -= 1
            elif sym == "[":
                counter2 += 1
            elif sym == "]":
                counter2 -= 1
            elif sym == "{":
                counter3 += 1
            elif sym == "}":
                counter3 -= 1

            if counter1 < 0 or counter2 < 0 or counter3 < 0:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
