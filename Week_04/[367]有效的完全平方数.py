# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。 
# 
#  说明：不要使用任何内置的库函数，如 sqrt。 
# 
#  示例 1： 
# 
#  输入：16
# 输出：True 
# 
#  示例 2： 
# 
#  输入：14
# 输出：False
#  
#  Related Topics 数学 二分查找 
#  👍 168 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 理解有偏差,我以为完全平方数是要全部都由一个最小的元素乘出来的。。。。。比如 16 = 2 * 2 * 2 * 2
# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         left, right, origin_num = 1, num, num
#         while left <= right:
#             mid = (left + right) // 2
#             if mid * mid == num:
#                 num = mid
#             if mid * mid < num:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#         while num <= origin_num:
#             if num * num == origin_num:
#                 return True
#             num = num * num
#
#         return False

# 1. 二分查找
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= num:
                left = mid + 1
            else:
                right = mid - 1

        return right * right == num

# 2. 牛顿迭代法   牛顿迭代法此处效率低于二分查找，为什么？
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = num
        while i * i > num:
            i = (i + num / i) // 2
        return i * i == num
# leetcode submit region end(Prohibit modification and deletion)
