# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法 
#  👍 396 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        check = [0 for i in range(len(nums))]

        def backtrack(sol, nums, check):
            if len(sol) == len(nums):
                res.append(sol)
                return

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                backtrack(sol + [nums[i]], nums, check)
                check[i] = 0

        backtrack([], nums, check)
        return res
# leetcode submit region end(Prohibit modification and deletion)
