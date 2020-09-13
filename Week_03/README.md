### 3 泛型递归、树的递归

#### 3.1 递归的实现、特性以及使用要点

> 递归-循环：通过函数体实现
>
> **关键点**：
>
> - 抵制人肉递归
> - 找最近重复子问题
> - 数学归纳法思想

##### 3.1.1 递归模板

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator                       1. 终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level             2. 当层处理过程 
    process(level, data...) 
    # drill down                                 3. 下钻
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed 4. 反转当前层状态
```

一般递归题只会用到递归模板中的前3步，按我自己的理解有些回溯题涉及到已经遍历过的元素，当需要回溯时就需要将当前层的状态回退到上一层，因此就需要第4步。具体的习题有：力扣[**第79题 单词搜索**](https://leetcode-cn.com/problems/word-search/)

##### 3.1.2 习题练习

1. [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/submissions/)

   > 简单的数学归纳，从如何到达最后一级台阶思考：
   >
   > - 可以从第n-1阶爬1阶到达第n阶
   > - 可以从第n-2阶爬2阶到达第n阶
   >
   > 假设爬到第n阶的方法为f(n)，那么爬到第n-1阶和第n-2阶的方法分别为f(n-1)和f(n-2)，则可得: f(n) = f(n-1) + f(n-2)
   >
   > 实现方法有两种：
   >
   > 1. 递归，注意建立hash表进行缓存，避免重复递归
   > 2. 迭代，根据递推公式进行迭代
   >
   > 时间复杂度 O(n)

2. [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

   > 括号的生成方式如下：
   >
   > 1. 只要左括号有剩余，均可添加"("
   > 2. 当左括号数量多于有括号时，可添加")"
   >
   > 时间复杂度 O(n)
   >
   > 递归终止条件是左括号和右括号均已全部使用。

3. [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/submissions/)

   > 简单的前序遍历，只需要把前序遍历模板中的访问根节点语句改为交换左右节点即可。时间复杂度 O(n)

4. [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/submissions/)

   > 在中序遍历，可以有3种做法：
   >
   > 1. 直接中序遍历，并将结果和排序后的数组进行比较，时间复杂度 O(n)，空间复杂度 O(n)。需要注意的是增加了一次排序过程 O(nlogn)，所以虽然同是 O(n) 但是效率不如第2种方法。
   > 2. 对1进行改进，其实不需要全部遍历完，由于二叉搜索树的中序遍历结果是一个单增序列，因此只需要比较当前节点的值和前一个节点的值即可，但需要一个初始化的最小值**float('-inf')** ,时间复杂度最坏情况是 O(n)，空间复杂度 O(1)。`提前终止条件很重要！！！`
   > 3. 手动维护一个栈，模拟中序遍历，时间复杂度和方法2相同(**是否相同?**)，实际运行效率不如方法2。

5. [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

   > 在遍历树的基础上同时更新树的深度即可，可使用前序遍历，中序遍历，后序遍历，层次遍历，DFS，BFS均可。

6. [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

   > 大体与二叉树的最小深度类似，不同的点在于:
   >
   > - 边界条件的处理
   > - 深度更新条件：仅当当前节点为叶节点(即左子树和右子树都为空)的时候，才更新。
   > - 提前终止条件：当本次递归的深度大于等于目前的最小深度时，终止递归。

7. [二叉树的序列化和反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)

   > 序列化：层次遍历
   >
   > 反序列化：参考构建堆的方式构建
   >
   > 问题：输入示例为[1, 2]时，正常的应该是根节点为1，左子树为2，但是序列化的结果出错了变成了[1, None, 2], 原因未知。

8. [二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

   > 深度优先搜索

9. [从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

   > 前序遍历： 根左右
   >
   > 中序遍历：左根右

10. [组合](https://leetcode-cn.com/problems/combinations/)

    > 递归，需要注意的是剪枝条件：当备选项不足时不再进行递归。



