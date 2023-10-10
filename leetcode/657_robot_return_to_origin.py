from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        right_counter = 0
        left_counter = 0
        up_counter = 0
        down_counter = 0
        for symbol in moves:
            if symbol == "R":
                right_counter += 1
            elif symbol == "L":
                left_counter += 1
            elif symbol == "U":
                up_counter += 1
            else:
                down_counter += 1

        if right_counter == left_counter and up_counter == down_counter:
            return True
        return False


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)

        if counter.get("L") == counter.get("R") and counter.get("U") == counter.get("D"):
            return True
        return False