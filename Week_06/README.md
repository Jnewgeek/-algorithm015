### week06 动态规划

> 1. 人肉递归低效、很累
> 2. 找到最近最简方法，将其拆解成可重复解决的问题
> 3. 数学归纳法思维(抵制人肉递归)

- 递归代码模板

```python
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

- 分治代码模板

```python
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

**关键点**

- `动态规划` 和 `递归`或者`分治`没有根本上的区别（关键看有无最优子结构）
- *共性*：找到重复子问题
- *差异性*：最优子结构，中途可以淘汰次优解。

小结

- 打破自己的思维惯性，形成机器思维

- 理解复杂逻辑的关键

  

#### DP 例题

1. Fibonacci数列

2. [不同路径](https://leetcode-cn.com/problems/unique-paths/)

   ```python
   # 二维状态矩阵
   dp[i][j] = dp[i+1][j] + dp[i][j+1]
   # 时间复杂度 n^2 空间复杂度 n^2
   
   # 压缩矩阵
   dp[i] += dp[i - 1]
   # 时间复杂度 n^2 空间复杂度 n
   
   class Solution:
       def uniquePaths(self, m: int, n: int) -> int:
           dp = [1] * n
           for i in range(1, m):
               for j in range(1, n):
                   dp[j] += dp[j - 1]
           return dp[-1]
   ```

3. [不同路径II](https://leetcode-cn.com/problems/unique-paths-ii/)

   增加了一个障碍物，当遇到障碍物时路径变为0，状态转移方程与不同路径基本一致。

   ```python
   class Solution:
       def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
           m, n = len(obstacleGrid), len(obstacleGrid[0])
           dp = [1] + [0] * n
           for i in range(m):
               for j in range(n):
                   dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j] + dp[j - 1]  # 最后一列0的作用在于如果j=0时else的时候索引不会超出范围
           return dp[-2]
   ```

4. [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)

   ```python
   class Solution:
       def longestCommonSubsequence(self, text1: str, text2: str) -> int:
           if not text1 or not text2:
               return 0
           m, n = len(text1), len(text2)
           dp = [[0] * (n + 1) for _ in range(m + 1)]
           for i in range(1, m + 1):
               for j in range(1, n + 1):
                   if text1[i - 1] == text2[j - 1]:
                       dp[i][j] = dp[i - 1][j - 1] + 1
                   else:
                       dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
           # print(dp)
           return dp[m][n]
   ```

   时间复杂度和空间复杂度都是 O(n^2)

   **尝试对dp状态矩阵进行压缩，发现当同一字符多次出现时会出现计数错误的情况发生，原因在于只有一行值的时候更新下一个元素之前错误地把前一个数改变了。**

   ```python
   class Solution:
       def longestCommonSubsequence(self, text1: str, text2: str) -> int:
           if not text1 or not text2:
               return 0
           m, n = len(text1), len(text2)
           dp = [0] * (n + 1)
           for i in range(1, m + 1):
               for j in range(1, n + 1):
                   if text1[i - 1] == text2[j - 1]:
                       dp[j] = min(dp[j - 1] + 1, i)
                   else:
                       dp[j] = min(max(dp[j], dp[j - 1]), i)
           # print(dp)
           return dp[-1]
   ```

5. [三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

   自底向上改变triangle的元素值，DP转移方程为:

   `dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])`

6. [最大子序列和](https://leetcode-cn.com/problems/maximum-subarray/)

   `dp[i] = max(0, dp[i - 1]) + nums[i]`

7. [乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

   需要保留最小的负数和最大的正数，因为负负得正的原因可能会导致最大的乘积发生变化。

   `ma =  max(ma, 1) * nums[i]`

   `mi = min(mi, 1) * nums[i]`

8. [零钱兑换](https://leetcode-cn.com/problems/coin-change/)

   - 暴力求解
   - BFS——找叶子节点，树的深度就是硬币的使用个数
   - DP

   ```python
   class Solution:
       def coinChange(self, coins: List[int], amount: int) -> int:
           MAX = float('inf')
           dp = [0] + [MAX] * amount
   
           for i in range(1, amount+ 1):
               dp[i] = min(dp[i - c] if i - c >= 0 else MAX for c in coins ) + 1
               # print(i, dp)
   
           return [dp[amount], -1][dp[amount] == MAX]
   ```

9. [打家劫舍](https://leetcode-cn.com/problems/house-robber/)

   相邻的不能偷，则状态转移方程为:

   `dp[i] =  max(dp[i - 2] + nums[i], dp[i - 1])`

   降低空间复杂度：

   `pre = now = 0`

   `pre, now = now, max(now, pre + nums[i])`

10. [打家劫舍II](https://leetcode-cn.com/problems/house-robber-ii/)

由于环的存在，如果偷了第一个则不能偷最后一个；偷了最后一个则不能偷第一个。因此可以进行分治，最后取最大值。

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            pre = now = 0
            for i in range(len(nums)):
                pre, now = now, max(now, pre + nums[i])
            return now
        return max(helper(nums[:-1]), helper(nums[1:]))
```

