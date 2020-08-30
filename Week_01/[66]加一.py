# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#  
# 
#  示例 2: 
# 
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#  
#  Related Topics 数组 
#  👍 531 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 移除末尾9即可
        for i in range(len(digits) - 1, -1, -1):
            # 倒序判断,该位为9则替换为0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # 将前一位加一
                digits[i] += 1
                break

        # 首位为0,进一位
        if digits[0] == 0:
            return [1] + digits
        return digits
# leetcode submit region end(Prohibit modification and deletion)
