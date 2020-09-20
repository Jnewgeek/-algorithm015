# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 506 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 1, x, 0
        while left <= right:
            mid = (left + right)//2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

# 牛顿迭代法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0

        C = x
        while True:
            xi = 0.5 * (x + C/x)
            if abs(xi - x) <= 1e-6:
                break
            x = xi
        return int(x)
# leetcode submit region end(Prohibit modification and deletion)
