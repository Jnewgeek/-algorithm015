# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 770 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1、 DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.m, self.n = len(grid), len(grid[0])
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

 # 2、 并查集
 class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        if not grid: return 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    for x, y in [[-1, 0], [0, -1]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                            union(tmp_i * row + tmp_j, i * row + j)
        # print(f)
        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res.add(find((i * row + j)))
        return len(res)
# leetcode submit region end(Prohibit modification and deletion)
