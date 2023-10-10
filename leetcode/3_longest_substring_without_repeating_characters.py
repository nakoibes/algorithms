class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_left = 0
        best_right = 0
        max_len = 0
        current_len = 0
        left = 0
        window = dict()
        for i in range(len(s)):
            if s[i] not in window:
                window[s[i]] = i
                current_len += 1
            else:
                max_len = max(current_len, max_len)
                # if current_len > max_len:
                #     best_left = left
                #     best_right = i
                #     max_len = current_len
                index = window[s[i]]
                new_left = index + 1
                window[s[i]] = i
                index -= 1
                while index != left - 1:
                    window.pop(s[index])
                    index -= 1

                left = new_left
                current_len = i - left + 1

        # if current_len > max_len:
        #     best_left = left
        #     best_right = i
        max_len = max(current_len, max_len)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        mp = dict()
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            res = max(res, j - i)
            mp[s[j]] = j
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        sym_dict = dict()
        for i in range(len(s)):
            if s[i] in sym_dict:
                left = max(left,sym_dict[s[i]] + 1)
            max_len = max(i - left + 1, max_len)
            sym_dict[s[i]] = i

        return max_len


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("abba"))
