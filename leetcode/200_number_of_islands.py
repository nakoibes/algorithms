from typing import List


class Solution:
    def is_in_islands(self, islands: list, point):
        for island in islands:
            if point in island:
                return island
        return None

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue

                if j - 1 < 0:
                    grid_left = "0"
                    left = 0
                else:
                    grid_left = grid[i][j - 1]
                    left = j - 1

                if j + 1 > n - 1:
                    grid_right = "0"
                    right = n - 1
                else:
                    grid_right = grid[i][j + 1]
                    right = j + 1

                if i - 1 < 0:
                    grid_up = "0"
                    up = 0
                else:
                    grid_up = grid[i - 1][j]
                    up = i - 1

                if i + 1 > m - 1:
                    grid_down = "0"
                    down = m - 1
                else:
                    grid_down = grid[i + 1][j]
                    down = i + 1
                # left = max(j - 1, 0)
                # right = min(j + 1, n)
                # up = max(0, i - 1)
                # down = min(m, i + 1)
                if (grid_left, grid_right, grid_up, grid_down) == ("0", "0", "0", "0"):
                    islands.append({(i, j)})
                else:

                    left_status = self.is_in_islands(islands, (i, left))
                    right_status = self.is_in_islands(islands, (i, right))
                    up_status = self.is_in_islands(islands, (up, j))
                    down_status = self.is_in_islands(islands, (down, j))
                    if left_status:
                        left_status.add((i, j))
                        continue
                    if right_status:
                        right_status.add((i, j))
                        continue
                    if up_status:
                        up_status.add((i, j))
                        continue
                    if down_status:
                        down_status.add((i, j))
                        continue
                    status = self.is_in_islands(islands, (i, j))
                    if not status:
                        islands.append({(i, j)})

        return len(islands)


if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grid = [["1"],["1"]]
    grid =[["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    print(s.numIslands(grid))
