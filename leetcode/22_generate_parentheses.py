from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()

        def add_parenthes(left, unmatched, s):
            if len(s) == 2 * n:
                result.append(s)
            elif left < n:
                add_parenthes(left + 1, unmatched + 1, s + "(")
            if unmatched > 0:
                add_parenthes(left, unmatched - 1, s + ")")

        add_parenthes(0, 0, "")
        return result

