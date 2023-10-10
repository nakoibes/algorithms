from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(s: str):
            num = int(s)
            if num > 255:
                return False
            if str(num) != s:
                return False
            return True

        if len(s) < 4 or len(s) > 12:
            return []

        result = list()

        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if i + j + k >= len(s):
                        continue
                    first = s[:i]
                    second = s[i:i + j]
                    third = s[i + j:i + j + k]
                    forth = s[i + j + k:]
                    if check(first) and check(second) and check(third) and check(forth):
                        result.append(first + "." + second + "." + third + "." + forth)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("0000"))
    print(s.restoreIpAddresses("101023"))
