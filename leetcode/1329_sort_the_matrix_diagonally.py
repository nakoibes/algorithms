from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """time - (m+n)*d*log(d), d = min(m,n);space - max(n,m)"""
        m = len(mat)
        n = len(mat[0])
        for k in range(m):
            if m <= n:
                diagonal_len = m - k
            else:
                if k <= m - n:
                    diagonal_len = n
                else:
                    diagonal_len = m - k
            diagonal = [mat[i + k][i] for i in range(diagonal_len)]
            diagonal.sort()
            for i in range(diagonal_len):
                mat[i + k][i] = diagonal[i]
        for k in range(1, n):
            if m <= n:
                if k <= n - m:
                    diagonal_len = m
                else:
                    diagonal_len = n - k
            else:
                diagonal_len = n - k
            diagonal = [mat[i][i + k] for i in range(diagonal_len)]
            diagonal.sort()
            for i in range(diagonal_len):
                mat[i][i + k] = diagonal[i]

        return mat


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """time - (m+n)*max(m,n)*log(max/2)?;space - n^2"""
        diagonals = defaultdict(list)
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])

        for diagonal in diagonals.values():
            diagonal.sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()

        return mat


if __name__ == '__main__':
    s = Solution()
    print(s.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
    # print(s.diagonalSort(
    #     [[58], [99], [1], [6], [73], [9], [60], [88], [64], [60], [39], [29], [46], [20], [78], [95], [2], [35], [20],
    #      [53], [60], [15], [94], [78], [26], [89], [87], [93], [70], [31], [94], [58], [90], [48], [60], [6], [68],
    #      [62], [32], [36], [73], [49], [45], [31], [23], [3], [73], [70], [71], [18], [14], [49], [84], [72], [59],
    #      [91], [17], [46], [93], [31], [31], [71], [52], [83], [8], [95], [49], [57], [52], [65], [83], [98], [46],
    #      [55], [44], [100], [45], [7], [59], [38], [82], [62], [25], [55], [64], [56], [89], [2], [10], [57], [26],
    #      [19], [27], [80], [12], [32], [62], [91], [68], [92]]))
    # print(s.diagonalSort(
    #     [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4],
    #      [84, 28, 14, 11, 5, 50]]))
