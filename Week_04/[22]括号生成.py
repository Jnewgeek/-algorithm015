# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1315 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0: return []
        queue, res = [(0, 0, '')], []
        while queue:
            left, right, tmp = queue.pop()
            if left == right == n:
                res.append(tmp)
            if left < n:
                queue.append((left + 1, right, tmp + '('))
            if left > right:
                queue.append((left, right + 1, tmp + ')'))
        return res
# leetcode submit region end(Prohibit modification and deletion)
