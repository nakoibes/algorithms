from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """time - nlogn; space - 1"""
        result = list()
        letters = dict()
        for i in range(len(s)):
            sym = s[i]
            if sym in letters:
                previous = letters[sym]
                letters[sym] = (previous[0], i)
            else:
                letters[sym] = (i, i)

        letters_list = list(letters.values())
        letters_list.sort(key=lambda x: x[0])

        right = letters_list[0][1]
        left = 0
        i = 1
        while right != len(s) - 1:
            current_sym = letters_list[i]
            if current_sym[0] > right:
                result.append(right - left + 1)
                right = current_sym[1]
                left = current_sym[0]
            elif current_sym[1] > right:
                right = current_sym[1]
            i += 1

        result.append(len(s) - left)
        return result


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """time - n; space - 1"""
        result = list()
        letters = dict()
        for i in range(len(s)):
            sym = s[i]
            if sym in letters:
                previous = letters[sym]
                letters[sym] = (previous[0], i)
            else:
                letters[sym] = (i, i)

        sym = letters[s[0]]
        right = sym[1]
        left = 0
        for i in range(1, len(s)):
            if i > right:
                result.append(right - left + 1)
                left = i
            sym = letters[s[i]]
            sym_right = sym[1]
            right = max(sym_right, right)

        result.append(len(s) - left)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
