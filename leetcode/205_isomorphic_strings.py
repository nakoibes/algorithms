from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translate = dict()
        s_symbols = set()
        for i in range(len(t)):
            t_sym = t[i]
            if t_sym not in translate:
                if s[i] in s_symbols:
                    return False
                translate[t_sym] = s[i]
                s_symbols.add(s[i])
            elif translate[t_sym] != s[i]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.isIsomorphic("egg", "add"))
    print(s.isIsomorphic("bbbaaaba", "aaabbbba"))
