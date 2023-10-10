from functools import lru_cache
from typing import List
import sys

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache
        def dp(i, j):
            if j == i:
                if n % 2 == 1:
                    return piles[i]
                else:
                    return -piles[i]

            if (j - i) % 2 != n % 2:
                a = piles[i] + dp(i + 1, j)
                b = piles[j] + dp(i, j - 1)
                return max(a, b)
            else:
                a = -piles[i] + dp(i + 1, j)
                b = -piles[j] + dp(i, j - 1)
                return min(a, b)

        return dp(0, len(piles) - 1) > 0


if __name__ == '__main__':
    s = Solution()
    p = [5, 100, 90, 2]
    print(s.stoneGame(p))
