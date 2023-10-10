def brute_force(string: str, word: str):
    for m in range(len(string) - len(word)):
        for i in range(len(word)):
            if word[i] != string[m + i]:
                break
        else:
            return m


def slow_prefix_function(string: str):
    p = [0] * len(string)
    for i in range(1, len(string)):
        for j in range(1, i + 1):
            if string[:j] == string[i - j + 1:i+1]:
                p[i] = j

    return p


def kmp(string: str, word: str) -> int:
    word_s = word + "#" + string
    print(slow_prefix_function(word_s))
    # print(word_s[-8])
    # j = 0
    # m = 0
    # # k = 0
    # while m < len(string) - len(word):
    #     i = j
    #     j = 0
    #     first = True
    #     while i < len(word):
    #         if string[m + i] == word[j] and not first:
    #             j += 1
    #         else:
    #             j = 0
    #         first = False
    #         if word[i] != string[m + i]:
    #             if i != 0:
    #                 i += 1
    #             break
    #         i += 1
    #
    #     else:
    #         return m
    #     if j == 0:
    #         m = m + i
    #     else:
    #         m = m + j


if __name__ == '__main__':
    print(kmp("ABCZABCDABZABCDABCDABDE", "ABCDABD"))
