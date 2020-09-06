# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。 
# 
# 
#  返回滑动窗口中的最大值。 
# 
#  
# 
#  进阶： 
# 
#  你能在线性时间复杂度内解决此题吗？ 
# 
#  
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window 
#  👍 535 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            # 滑动窗口边界移动单次循环只会发生一次
            if deque and deque[0] <= i - k:deque.popleft() # outdate indices
            # 双端队列中只记录单调递减的值的索引
            while deque and num > nums[deque[-1]]:deque.pop()
            deque.append(i)
            # 共有n-k+1个最大值
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res
# leetcode submit region end(Prohibit modification and deletion)
