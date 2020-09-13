# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 882 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        def backtrack(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i,j in enumerate(nums):
                    backtrack(nums[:i] + nums[i+1:], temp +[j])

        backtrack(nums, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
