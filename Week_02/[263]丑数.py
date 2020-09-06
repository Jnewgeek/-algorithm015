# 编写一个程序判断给定的数是否为丑数。 
# 
#  丑数就是只包含质因数 2, 3, 5 的正整数。 
# 
#  示例 1: 
# 
#  输入: 6
# 输出: true
# 解释: 6 = 2 × 3 
# 
#  示例 2: 
# 
#  输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
#  
# 
#  示例 3: 
# 
#  输入: 14
# 输出: false 
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。 
# 
#  说明： 
# 
#  
#  1 是丑数。 
#  输入不会超过 32 位有符号整数的范围: [−231, 231 − 1]。 
#  
#  Related Topics 数学 
#  👍 148 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:  ## 如果num非正，就不是丑数
            return False
        while True:
            last = num
            if not num % 2:  ## 如果2整除num，就除以2
                num >>= 1
            if not num % 3:  ## 如果3整除num，就除以3
                num //= 3
            if not num % 5:  ## 如果5整除num，就除以5
                num //= 5
            if num == 1:  ## 如果若干次操作后，num变成1，说明num的因数只有2、3、5，是丑数
                return True
            if last == num:  ## 如果1轮操作后，num没变，说明num不是丑数
                return False
# leetcode submit region end(Prohibit modification and deletion)
