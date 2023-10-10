class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        left = 0
        right = k - 1
        current_dict = dict()
        for i in range(min(k, len(s))):
            current_dict[s[i]] = current_dict.get(s[i], 0) + 1

        max_len = len(current_dict)
        current_len = k
        while right != len(s) - 1:
            if len(current_dict) <= k:
                max_len = max(max_len, current_len)
                current_dict[s[right + 1]] = current_dict.get(s[right + 1], 0) + 1
                current_len += 1
                right += 1
            else:
                current_dict[s[left]] -= 1
                if current_dict[s[left]] == 0:
                    current_dict.pop(s[left])
                left += 1
                current_len -= 1

        if len(current_dict) <= k:
            max_len = max(max_len, current_len)

        return max_len


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstringKDistinct("eceba", 2))
    print(s.lengthOfLongestSubstringKDistinct("aa", 1))
