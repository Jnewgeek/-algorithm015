## 1. 哈希表、映射、集合

哈希表(Hash table): 散列表，根据关键码值而直接进行访问的数据结构，使用哈希函数，一般认为查询时间复杂度为**O(1)**。

哈希碰撞(经过哈希函数得到相同的键值)的常用解决方式：

- 依次向下存储，占用其他的位置
- 拉链式解决冲突法：一个键值对应的是一个链表，当链表较长时，查询效率退化至**O(n)**。

#### 习题练习

1. 有效的字母异位词

   ```python
   # 思路: 遍历第一个字符串构造哈希表进行字母计数，再遍历第二个字符串对字母数量做减法，最后判断哈希表是否为空
   class Solution:
       def isAnagram(self, s: str, t: str) -> bool:
           s1 = {}
           for i in s:
               s1[i] = s1.get(i, 0) + 1
           for i in t:
               s1[i] = s1.get(i, 0) - 1
               if s1[i] == 0:
                   del s1[i]
           return s1 == {}
   ```

2. 字母异位词分组

   ```python
   # 思路: 遍历列表，对每个字符串排序后作为键，字符串本身作为值构造哈希表，最后输出哈希表中的所有值。
   from collections import defaultdict
   class Solution:
       def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           my_dict = defaultdict(list)
           for i in strs:
               my_dict["".join(sorted(i))].append(i)
           return list(my_dict.values())
   ```

3. 两数之和

   ```python
   # 思路: 遍历列表，更新哈希表({值:索引})，如果哈希表中存在指定的值，则输出两个数的索引位置。
   class Solution:
       def twoSum(self, nums: List[int], target: int) -> List[int]:
           my_dict = {}
           for i,j in enumerate(nums):
               if my_dict.get(target - j, None) is not None:
                   return [my_dict[target - j], i]
               else:
                   my_dict[j] = i
           return []
   ```

## 2. 树、二叉树、二叉搜索树

**`加速的关键在于升维。`**

- 链表是特殊化的树；

- 树是特殊化的图。

#### 2.1 二叉树的遍历方式

1. 前序遍历（Pre-order）：根左右
2. 中序遍历（In-order）：左根右
3. 后序遍历（Post-order）：左右根

注：为便于记忆，三种遍历方式的次序均相对于根节点，即先遍历根节点还是后遍历根节点。

#### 2.2 代码实现——Python

```python
# 树定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:

    def __init__(self):
        self.res = []
	
    # 1. 前序遍历
	def preorder(self, root):
        if root:
            self.res.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
        return self.res
            
    # 2. 中序遍历
	def preorder(self, root):
        if root:
            self.preorder(root.left)
            self.res.append(root.val)
            self.preorder(root.right)
        return self.res
            
    # 3. 后序遍历
	def preorder(self, root):
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
            self.res.append(root.val)
        return self.res
```

#### 2.3 二叉搜索树

二叉搜索树，也称为二叉排序树、有序二叉树、排序二叉树，是指一棵空树或者具有以下性质的二叉树：

1. 左子树上的**所有节点**的值均小于它的根节点的值；

2. 右子树上的**所有节点**的值均大于它的根节点的值；

3. 以此类推，左、右子树也分别为二叉搜索树。

   中序遍历：升序排列

#### 2.4 习题练习

1. 二叉树的中序遍历

   ```python
   # 解法1 : 递归算法
   # 解法2 : 迭代算法，手动维护一个栈
   class Solution:
       def inorderTraversal(self, root: TreeNode) -> List[int]:
           stack, res = [root], []
           while stack:
               node = stack.pop()
               if isinstance(node, TreeNode):
                   stack.extend([node.right, node.val, node.left])
               elif isinstance(node, int):
                   res.append(node)
               else:
                   continue
   
           return res
   ```

   前序遍历和后序遍历的实现类似，只需要调整插入顺序即可。

2. N叉树的前序遍历

   ```python
   # 思路: 递归算法，和二叉树不同的点在于N叉树中不能再用left和right遍历子树
   # 通过缓存的方式，减少递归次数。
   class Solution:
   
       def __init__(self):
           self.res = []
           # 记录已经访问过的节点
           self.record=set()
   
       def preorder(self, root: 'Node') -> List[int]:
           if root in self.record:
               return
           if root:
               self.record.add(root)
               self.res.append(root.val)
               if isinstance(root.children, list):
                   for i in root.children:
                       self.preorder(i)
               else:
                   self.preorder(root.children)
           return self.res
   ```

   

3. N叉树的层序遍历(广度优先算法和深度优先算法)

   ```python
   # 解法1: 深度优先搜索 DFS
   class Solution:
       def levelOrder(self, root: 'Node') -> List[List[int]]:
   
           res = []
           def dfs(root, depth):
               if not root:
                   return
               # 进入下一层, 初始化
               if len(res) <= depth:
                   res.append([])
               # 由于有depth下标的存在,因此append的时候不会出错
               res[depth].append(root.val)
               for ch in root.children:
                   dfs(ch, depth + 1)
   
           dfs(root, 0)
           return res
   
   # 解法2: 广度优先搜索 BFS
   # 从运行结果上看, 对于层次遍历来说，广度优先算法耗时更短，但需要额外的存储空间。
   class Solution:
       def levelOrder(self, root: 'Node') -> List[List[int]]:
           if not root: return
           res = []
           def dfs(root):
               queue = [root]
               while queue:
                   tmp = []
                   nxt =[]
                   for i in queue:
                       tmp.append(i.val)
                       for ch in i.children:
                           nxt.append(ch)
                   res.append(tmp)
                   queue = nxt
   
           dfs(root)
           return res
   ```

   

## 3. 堆和二叉树、图

堆(Heap): 可以迅速找到最大值或最小值的数据结构，常见的有二叉堆，斐波那契堆。

常见操作(以大根堆为例)：

- find-max: O(1)
- delete-max: O(logn)
- insert(create): O(logn) or O(1)

#### 3.1 二叉堆

通过完全二叉树实现（注意不是二叉搜索树，即不满足中序遍历即升序排列的特性）；

二叉堆（大顶堆）满足以下性质：

- 是一棵完全树
- 树中任意节点的值总是>=其子节点的值

**二叉堆的实现细节**

- 二叉堆一般通过数组实现
- 假设第一个元素的索引为0，则父节点和子节点的关系为：
  - 索引为i的左孩子的索引为 2*i+1
  - 索引为i的右孩子的索引为 2*i+2
  - 索引为i的父节点的索引为 floor((i-1)/2)

**Insert 插入操作**

- 新元素一律先插到数组最后
- 依次向上浮动，和父亲节点进行比较并进行互换，更新二叉堆，时间复杂度为O(logn)即树的深度。

**deletmax删除堆顶操作**

- 将堆尾元素替换到顶部
- 依次从根部向下调整整个堆的结构

#### 3.2 习题练习

1. 最小的K个数

   ```python
   # 解法1: sort排序: 时间复杂度 O(nlogn)
   class Solution:
       def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
           return sorted(arr)[:k]
   
   # 解法2: 小根堆, 调用模块, 时间复杂度 O(nlogk)
   # 实际运行结果效率低于直接排序，不知道为什么？
   import heapq
   class Solution:
       def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
           if not arr: return []
           if len(arr) <= k: return arr
           return heapq.nsmallest(k, arr)
   
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
   ```

   

2. 滑动窗口最大值

   ```python
   # 思路: 参考示例代码， 使用双端队列维护一个单调递减序列， 并在窗口发生移动时添加窗口内的最大值。
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
   ```

   

3. 丑数

   ```python
   # 思路: 动态规划，参考示例代码
   
   class Solution:
       def nthUglyNumber(self, n: int) -> int:
           dp, a, b, c = [1] * n, 0, 0, 0
           for i in range(1, n):
               n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
               dp[i] = min(n2, n3, n5)
               if dp[i] == n2: a += 1
               if dp[i] == n3: b += 1
               if dp[i] == n5: c += 1
           return dp[-1]
   ```

   详细题解：https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/

4. 前K个高频元素

   ```python
   # 解法1: 大根堆
   class Solution:
       def topKFrequent(self, nums: List[int], k: int) -> List[int]:
           dic = Counter(nums)
           queue, res = [], []
           for i in dic:
               heapq.heappush(queue, (-dic[i], i))
           for i in range(k):
               tmp = heapq.heappop(queue)
               res.append(tmp[1])
           return res
   
   # 解法2: 大根堆
   class Solution:
       def topKFrequent(self, nums: List[int], k: int) -> List[int]:
           # hash表统计个数
           my_dict = {}
           for i in nums:
               my_dict[i] = my_dict.get(i, 0) + 1
   
           iter = my_dict.items()
           # 大根堆
           heap = heapq.nlargest(k, iter, key = lambda x: x[1])
           return [j for j, i in heap]
   ```

   

图相关的未看完，笔记暂无。