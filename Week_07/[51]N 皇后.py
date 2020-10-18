# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例： 
# 
#  输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  Related Topics 回溯算法 
#  👍 642 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return

            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    backtrack(queens + [q], xy_diff + [p-q], xy_sum + [p+q])
        res = []
        backtrack([], [], [])
        return [['.'*i+'Q'+'.'*(n-i-1) for i in sol] for sol in res]
# leetcode submit region end(Prohibit modification and deletion)
