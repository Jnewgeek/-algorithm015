# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1229 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 方法1: 递归
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        # 避免重复递归,建立hash表
        hash_map = {1:1, 2:2, 3:3}
        # f1 = 1, f2 = 2, f3 = f1 + f2 = 3
        def backtrack(n):
            if n <= 3:
                return hash_map[n]

            if n not in hash_map:
                hash_map[n] = backtrack(n - 1) + backtrack(n - 2)
            return hash_map[n]

        backtrack(n)
        return hash_map[n]

# 方法2: 迭代
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return n

        f1, f2, f3 = 1, 2, 3
        for i in range(4, n + 1):
            f1, f2 = f2, f3
            f3 = f1 + f2
        return f3
# leetcode submit region end(Prohibit modification and deletion)
