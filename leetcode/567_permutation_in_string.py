class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = dict()
        for letter in s1:
            s1_dict[letter] = s1_dict.get(letter, 0) + 1

        window = dict()

        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if window == s1_dict:
            return True

        next_index = len(s1)
        left = 0

        while next_index < len(s2):
            if s2[left] == s2[next_index]:
                left += 1
                next_index += 1
                continue
            elif s2[next_index] not in s1_dict:
                if len(s2) - next_index - 1 >= len(s1):
                    left = next_index + 1
                    next_index = left + len(s1)
                    new_dict = dict()
                    for i in range(left, left + len(s1)):
                        new_dict[s2[i]] = new_dict.get(s2[i], 0) + 1
                    window = new_dict
                else:
                    break
            else:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    window.pop(s2[left])
                window[s2[next_index]] = window.get(s2[next_index], 0) + 1
                left += 1
                next_index += 1

            if window == s1_dict:
                return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = dict()
        for letter in s1:
            s1_dict[letter] = s1_dict.get(letter, 0) + 1

        window = dict()

        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if window == s1_dict:
            return True

        next_index = len(s1)
        left = 0

        counter = 0
        for letter in s1_dict:
            if window.get(letter, 0) == s1_dict.get(letter, 0):
                counter += 1
        while next_index < len(s2):
            if s2[left] == s2[next_index]:
                left += 1
                next_index += 1
                continue
            elif s2[next_index] not in s1_dict:
                if len(s2) - next_index - 1 >= len(s1):
                    left = next_index + 1
                    next_index = left + len(s1)
                    new_dict = dict()
                    for i in range(left, left + len(s1)):
                        new_dict[s2[i]] = new_dict.get(s2[i], 0) + 1
                    window = new_dict
                    if window == s1_dict:
                        return True
                    counter = 0
                    for letter in s1_dict:
                        if window.get(letter, 0) == s1_dict.get(letter, 0):
                            counter += 1
                else:
                    break
            else:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    window.pop(s2[left])
                window[s2[next_index]] = window.get(s2[next_index], 0) + 1

                if window.get(s2[left], 0) == s1_dict.get(s2[left], 0) and s2[left] in s1_dict:
                    counter += 1
                elif window.get(s2[left], 0) == s1_dict.get(s2[left], 0) - 1 and s2[left] in s1_dict:
                    counter -= 1
                if window.get(s2[next_index], 0) == s1_dict.get(s2[next_index], 0):
                    counter += 1
                elif window.get(s2[next_index], 0) == s1_dict.get(s2[next_index], 0) + 1:
                    counter -= 1
                if counter == len(s1_dict):
                    return True
                left += 1
                next_index += 1

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("rvwrk", "lznomzggwrvrkxecjaq"))
