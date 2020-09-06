# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#  
# 
#  示例 2： 
# 
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0] 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= k <= arr.length <= 10000 
#  0 <= arr[i] <= 10000 
#  
#  Related Topics 堆 分治算法 
#  👍 127 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 解法1: sort排序: 时间复杂度 O(nlogn)
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]

# 解法2: 大根堆, 调用模块, 时间复杂度 O(nlogk)
# 实际运行结果效率低于直接排序，不知道为什么？

# import heapq
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         if not arr: return []
#         if len(arr) <= k: return arr
#         return heapq.nsmallest(k, arr)

# 解法3: 示例代码，手写大根堆, 时间复杂度 O(nlogk)
# 实际运行效果也低于直接排序。

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k==0: return []    # 测试样例中k可能等于0,开始未考虑道导致出错
        if len(arr) <= k: return arr
        heap = arr[:k]
        # 构建大根堆
        def buildMaxHeap(pos):
            # 临时存储, 不需要每次都将两个值进行互换, 只在最后将存储的父亲节点的值放到合适的位置
            while 2 * pos + 1 < k:
                max_pos = 2 * pos + 1
                # 比较左右儿子, 将较大者与父亲节点互换
                if 2 * pos + 2 < k and heap[2 * pos + 2] > heap[2 * pos + 1]:
                    max_pos += 1
                if heap[max_pos] > heap[pos]:
                    heap[max_pos], heap[pos] = heap[pos], heap[max_pos]
                    pos = max_pos
                else:
                    break

        # 初始化一个大根堆
        for i in range(k//2, -1, -1):
            buildMaxHeap(i)

        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]   # 如果后面的值比大根堆里的最大值要小才有更新的必要
                buildMaxHeap(0)    # 更新大根堆
            else:
                continue

        return heap
# leetcode submit region end(Prohibit modification and deletion)
