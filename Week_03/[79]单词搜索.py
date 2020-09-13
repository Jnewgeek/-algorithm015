# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法 
#  👍 585 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:   # 边界条件
            return False
        m, n = len(board), len(board[0])

        def dfs(i, j, word):
            if len(word) == 0:   # 成功匹配
                return True
            if not(0 <= i < m and 0 <= j < n and word[0] == board[i][j]):  # 超出索引范围,字母不匹配
                return False
            temp = board[i][j] # 临时变量保存字母
            board[i][j] = '#'  # 将已经遍历过的位置字母替换为#
            # 上下左右遍历
            res = dfs(i + 1, j, word[1:]) or dfs(i - 1, j, word[1:]) or dfs(i, j - 1, word[1:]) or dfs(i, j + 1, word[1:])

            # 重置当前层的条件
            board[i][j] = temp

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
