# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2522 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先排序
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        target = []              # 开始直接设置的[]，发现陷入了死循环，原因是else之后i和j的数字不再发生变化
        for k in range(0, len(nums)-2):
            if nums[k] > 0:
                break
            # 跳过相同数字，开始未设置导致超出时间限制
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                sum_ = nums[k] + nums[i] + nums[j]   # 求和
                if sum_ < 0:
                    i += 1
                elif sum_ > 0:
                    j -= 1
                else:
                    target.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
        return target
# leetcode submit region end(Prohibit modification and deletion)
