# Хранить 2 строки, не обрабатывать края, сразу искать максимум
def find_longest_common_substring(s1: str, s2: str):
    matrix = [[0] * len(s2) for _ in range(len(s2))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == 0 or j == 0:
                matrix[i][j] = int(s1[i] == s2[j])
            else:
                if s1[i] == s2[j]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = 0
    max_len = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            max_len = max(matrix[i][j], max_len)

    return max_len


def find_longest_common_subsequence(s1: str, s2: str):
    matrix = [[0] * len(s2) for _ in range(len(s2))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == 0:
                if j == 0:
                    matrix[i][j] = int(s1[i] == s2[j])
                else:
                    matrix[i][j] = max(int(s1[i] == s2[j]), matrix[i][j - 1])
            if j == 0:
                if i == 0:
                    matrix[i][j] = int(s1[i] == s2[j])
                else:
                    matrix[i][j] = max(int(s1[i] == s2[j]), matrix[i - 1][j])

            if i != 0 and j != 0:
                if s1[i] == s2[j]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    max_len = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            max_len = max(matrix[i][j], max_len)

    return max_len


if __name__ == '__main__':
    # print(find_longest_common_substring("blue", "clue"))
    print(find_longest_common_substring("afish", "ahish"))
    print(find_longest_common_subsequence("afishnt", "ahishmy"))
