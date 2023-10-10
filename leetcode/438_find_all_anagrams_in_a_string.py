from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        k = len(p)
        word_dict = dict()
        search_dict = dict()
        last_success = False
        for letter in p:
            word_dict[letter] = word_dict.get(letter, 0) + 1

        for i in range(len(p)):
            search_dict[s[i]] = search_dict.get(s[i], 0) + 1

        result = list()

        if search_dict == word_dict:
            last_success = True
            result.append(0)

        left = 0
        next_symbol_index = left + k

        while next_symbol_index <= len(s) - 1:
            if s[next_symbol_index] not in word_dict and next_symbol_index <= len(s) - k - 1:
                left = next_symbol_index + 1
                next_symbol_index = left + k
                new_search_dict = dict()
                for i in range(left, next_symbol_index):
                    new_search_dict[s[i]] = new_search_dict.get(s[i], 0) + 1
                search_dict = new_search_dict
            elif s[next_symbol_index] == s[left]:
                if last_success:
                    result.append(left + 1)
                left += 1
                next_symbol_index += 1
                continue
            else:
                search_dict[s[next_symbol_index]] = search_dict.get(s[next_symbol_index], 0) + 1
                search_dict[s[left]] -= 1
                if search_dict[s[left]] == 0:
                    search_dict.pop(s[left])
                left += 1
                next_symbol_index += 1

            if search_dict == word_dict:
                last_success = True
                result.append(left)
            else:
                last_success = False

        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.findAnagrams("abab", "ab"))
    # print(s.findAnagrams("cbaebabacd", "abc"))
    # print(s.findAnagrams("ababababab", "aab"))
    # print(s.findAnagrams("aecbabedce", "a"))
    # print(s.findAnagrams("abcabccbbaa", "aabbcc"))
    print(s.findAnagrams("ababababa", "ab"))
