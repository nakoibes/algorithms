'''premium'''


# Given two strings s and t, determine if they are both one edit distance apart.

def main(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False

    if len(s) == len(t):
        bad_symbol = False
        for s_letter, t_letter in zip(s, t):
            if s_letter != t_letter and bad_symbol:
                return False
            elif s_letter != t_letter and not bad_symbol:
                bad_symbol = True
        if bad_symbol:
            return True
        return False

    if len(s) < len(t):
        s, t = t, s

    i = 0
    j = 0
    bad_symbol = False
    while i < len(s):
        if s[i] != t[j] and not bad_symbol:
            i += 1
            continue
        elif s[i] != t[j] and bad_symbol:
            return False
    return True


def suffix_equal(s: str, t: str, s_start: int, t_start: int) -> bool:
    i = s_start
    j = t_start
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            return False

    return True


def main(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False
    if len(s) < len(t):
        return main(t, s)

    for i in range(len(t)):
        if s[i] != t[i]:
            if len(s) == len(t):
                return suffix_equal(s, t, i + 1, i + 1)
            else:
                return suffix_equal(s, t, i, i + 1)

    if len(s) != len(t):
        return True
    return False


def main(s: str, t: str) -> bool:
    s_len = len(s)
    t_len = len(t)
    min_len = min(s_len, t_len)
    i = 0
    while i < min_len and s[i] == t[i]:
        i += 1

    j = 0
    while j < min_len - i and s[s_len - 1 - j] == t[t_len - 1 - j]:
        j += 1

    return s_len + t_len - min_len - 1 == i + j


if __name__ == '__main__':
    # s = input()
    # t = input()

    # print(main(s, t))

    def test():
        tests = [(("ab", "acb"), True), (("cab", "ad"), False), (("1203", "1213"), True), (("123", "12345"), False),
                 (("123", "223"), True), (("123", "123"), False), (("123", "124"), True), (("abcd", "bcd"), True),
                 (("abcde", "bcee"), False), (("abcde", "abce"), False)]
        for i, test in enumerate(tests):
            if test[1] != main(*test[0]):
                print(i)
