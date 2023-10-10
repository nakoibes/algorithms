from random import randint
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a_set = {A[0], }
        b_set = {B[0], }
        c = [0] * len(A)
        if A[0] == B[0]:
            c[0] = 1
        else:
            c[0] = 0
        for i in range(1, len(A)):

            c[i] = c[i - 1]
            if A[i] == B[i]:
                c[i] += 1
            else:
                if A[i] in b_set:
                    c[i] += 1
                if B[i] in a_set:
                    c[i] += 1

            a_set.add(A[i])
            b_set.add(B[i])

        return c


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        union = set()
        c = [0] * len(A)
        for i in range(len(A)):
            union.add(A[i])
            union.add(B[i])
            c[i] = (i + 1) * 2 - len(union)

        return c


class Solution1:
    """Not permutation"""

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a_set = {A[0], }
        b_set = {B[0], }
        intersection = set()
        c = [0] * len(A)
        if A[0] == B[0]:
            c[0] = 1
            intersection.add(A[0])
        else:
            c[0] = 0
        for i in range(1, len(A)):
            c[i] = c[i - 1]
            if A[i] == B[i] and A[i] not in intersection:
                c[i] += 1
                intersection.add(A[i])
            else:
                if A[i] in b_set and A[i] not in intersection:
                    c[i] += 1
                    intersection.add(A[i])
                if B[i] in a_set and B[i] not in intersection:
                    intersection.add(B[i])
                    c[i] += 1

            a_set.add(A[i])
            b_set.add(B[i])

        return c

    def slow_solution(self, A: List[int], B: List[int]) -> List[int]:
        a_set = set()
        b_set = set()
        c = [0] * len(A)
        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])
            c[i] = len(a_set.intersection(b_set))
        return c


if __name__ == '__main__':
    def stress_test():
        for _ in range(100_000):
            n = randint(1, 30)
            seq1 = [randint(-30, 30) for i in range(n)]
            seq2 = [randint(-30, 30) for i in range(n)]
            s = Solution1()
            if s.slow_solution(seq1, seq2) != s.findThePrefixCommonArray(seq1, seq2):
                print("WA")
                break


    def stress_test2():
        s1 = Solution1()
        s = Solution()
        for _ in range(100_000):
            n = randint(1, 30)
            seq1 = list()
            seq2 = list()
            while len(seq1) != n:
                num = randint(-100, 100)
                if num not in seq1:
                    seq1.append(num)
            while len(seq2) != n:
                num = randint(-100, 100)
                if num not in seq2:
                    seq2.append(num)
            # seq1 = [ for i in range(n)]
            # seq2 = [randint(-30,30) for i in range(n)]

            if s.findThePrefixCommonArray(seq1, seq2) != s.findThePrefixCommonArray(seq1, seq2):
                print("WA")
                break


    s = Solution1()
    # print(s.findThePrefixCommonArray([1, 2, 3, 4, 2, 199],
    #                                  [2, 1, 3, 2, 2, 2, ]))
    # print(s.slow_solution([1, 2, 3, 4, 2, 199],
    #                       [2, 1, 3, 2, 2, 2, ]))
    stress_test2()
