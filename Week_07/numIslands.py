"""
    @:argument 1. 通过dfs实现岛屿数量
               2. 通过并查集实现岛屿数量
"""


class Solution(object):
    def numIslands(self, grid):
        """
        1. DFS 实现岛屿数量
        :param grid: list
        :return: int
        """
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)


class NewSolution:
    def newNumIslands(self, grid: list):
        """
        2. 并查集实现岛屿数量
        :param grid: list
        :return: int
        """
        f = {}
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    for x, y in [[-1, 0], [0, -1]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == '1':
                            union(tmp_i * row + tmp_j, i * row + j)
        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res.add(find(i * row + j))
        return len(res)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    s = Solution()
    print(s.numIslands(grid=grid))

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    ss = NewSolution()
    print(ss.newNumIslands(grid))
