from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = list()
        last_char = chars[0]
        counter = 1
        # second_time = 1
        for i in range(1, len(chars)):
            if chars[i] != last_char and counter == 1:
                s.append(last_char)
                last_char = chars[i]

            elif chars[i] != last_char and counter > 1:
                s.append(last_char)
                for digit in str(counter):
                    s.append(digit)
                counter = 1
                last_char = chars[i]

            elif chars[i] == last_char:
                counter += 1

        if counter == 1:
            s.append(last_char)
        else:
            s.append(last_char)
            for digit in str(counter):
                s.append(digit)

        for i in range(len(chars)):
            chars.pop()
        for i in range(len(s)):
            chars.append(s[i])
        # chars = s.copy()

        return len(s)


class Solution:
    def compress(self, chars: List[str]) -> int:
        last_char = chars[0]
        counter = 1
        left = 0
        for i in range(1, len(chars)):
            if chars[i] != last_char and counter == 1:
                chars[left] = last_char
                last_char = chars[i]
                left += 1

            elif chars[i] != last_char and counter > 1:
                chars[left] = last_char
                left += 1
                for digit in str(counter):
                    chars[left] = digit
                    left += 1
                counter = 1
                last_char = chars[i]
            elif chars[i] == last_char:
                counter += 1

        if counter != 1:
            chars[left] = last_char
            left += 1
            for digit in str(counter):
                chars[left] = digit
                left += 1
        else:
            chars[left] = last_char
            left += 1

        # for _ in range(len(chars) - 1, left - 1, -1):
        #     chars.pop()

        return len(chars)

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res

if __name__ == '__main__':
    s = Solution()
    seq = ["a", "a", "b", "b", "c", "c", "c"]
    # print(s.compress(seq))
    # print(seq)

    # seq = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    # seq = ["a", "a", "a", "a", "b", "a"]
    print(s.compress(seq))
    print(seq)
