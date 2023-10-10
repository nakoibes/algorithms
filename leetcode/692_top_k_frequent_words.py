from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """time - nlogn, space - n"""
        words_dict = dict()
        result = list()
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        frequencies_dict = defaultdict(list)
        for word, frequency in words_dict.items():
            frequencies_dict[frequency].append(word)

        frequencies = list(frequencies_dict.keys())
        frequencies.sort(reverse=True)
        for frequency in frequencies:
            if k > 0:
                if k - len(frequencies_dict[frequency]) >= 0:
                    result.extend(sorted(frequencies_dict[frequency]))
                    k -= len(frequencies_dict[frequency])
                else:
                    # residual = len(frequencies_dict[frequency])-k
                    result.extend(sorted(frequencies_dict[frequency])[:k])
                    break
            else:
                break

        return result


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """time - nlogk?(nlogn), space - n"""
        words_dict = dict()
        result = list()
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        maxheap = list()
        for word, frequency in words_dict.items():
            heappush(maxheap, [-frequency, word])

        for _ in range(k):
            frequency, word = heappop(maxheap)
            result.append(word)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(["ab", "aa"], 1))
