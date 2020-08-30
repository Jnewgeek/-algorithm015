## Week01 学习笔记

#### 作业部分

1.[【1】两数之和 - 简单](https://leetcode-cn.com/problems/two-sum/)
   > 以空间换时间，构造字典来进行检索

   ```(python)
   my_dict={}                    # 构造字典
   for i,num in enumerate(nums):
       if my_dict.get(target-num) is not None:
       	return [my_dict[target-num],i]
       my_dict[num]=i
   return []
   ```

2. [【26】删除排序数组中的重复项 - 简单](https://leetcode-cn.com/problems/container-with-most-water/])

	> 使用快慢双指针替换元素，降低时间复杂度

3. [【11】盛最多水的容器 - 中等](https://leetcode-cn.com/problems/container-with-most-water/)
   
	> 容量计算公式: S=min(height[left]\*height[right])\*(right-left+1)，使用双指针确定左右边界，且水的高度取决于较短的垂线，从公式中可以得知，当左右两边的指针向中间收敛时，必须是高度较矮的垂线先向中间移动，才有可能使得width减少的情况下容量S上升。

4. [【15】三数之和 - 中等](https://leetcode-cn.com/problems/3sum/)
   
   > 暴力求解时间复杂度为O(n^3)超时，先对数组进行排序，之后采用双指针的方式遍历数组，并在遍历过程中跳过重复元素，降低遍历次数。 

5. [【20】有效的括号 - 简单](https://leetcode-cn.com/problems/valid-parentheses/)
   
   > 栈可以解决最近相似情况的一类问题。
6. [【21】合并两个有序链表 - 简单](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
   
   > 以空间换时间，建立数组对链表元素进行排序，再添加到新链表中
7. [【24】两两交换链表中的节点 - 简单](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
   
   > 交换指针的指向关系，本质上是: a, b = head, head.next，a.next, b.next = b.next, a
8. [【26】删除排序数组中的重复项 - 简单](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
   
   > 双指针，交换数组元素
9. [【66】加一 - 简单](https://leetcode-cn.com/problems/plus-one/)
   
   > 多种方法均可实现，(1) 移除末尾为9的元素并补齐0 ；(2) 计数并记录进位；两种方法最后都需要注意首位变为0时需要在最前方添加1


10. [【70】爬楼梯 - 简单](https://leetcode-cn.com/problems/climbing-stairs/)
   > 归纳与演绎，当用户处于第N级阶梯时，他仅有两种可能方式从之前的阶梯上来，即从第N-1级走1级阶梯或者从第N-2级走两级阶梯，递推公式即为斐波那契数列


11. [【84】柱状图中最大的矩形 - 困难](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
   > 开始以为可以用第11题中的双指针求解，但忽视了左右边界中间的矩形高度不能低于两个边界，因此需要加多一层判定边界以内的矩形高度都至少都等于边界，理论上时间复杂度为O(n^2)，实际实现过程中发现超时。题解中的采用单调栈遍历数组的思想之后还需要多理解和复现几遍才能掌握


12. [【88】合并两个有序数组 - 简单](https://leetcode-cn.com/problems/merge-sorted-array/)
   > 替换数组元素再排序即可实现

13. [【141】环形链表 - 简单](https://leetcode-cn.com/problems/linked-list-cycle/)
   > 借助hash表即可实现

14. [【142】环形链表II - 中等](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
   > (1) hash表可以实现；(2) 不增加额外存储空间的话，需要采用快慢指针fast，slow: 当fast指针再次追上slow指针时，fast走过的步数是slow的两倍即 f = 2\*s，假设链表中头指针到环入口的步数是a, 环的长度为b，那么fast比slow多走了n个环长度，则fast走过的步数为 f = s + nb，两式相减得f  = 2nb，s = nb，而从链表头部出发走到环入口的步数始终为k = a+nb，而当前slow指针已经走了nb步，因此只需要再走a步即可到达入口，虽然a未知但是链表头部到环入口的步数正好是a，所以当fast和slow第一次重合时，fast从头开始走，当fast和slow再次重合时，此时fast和slow所在的位置就是环入口。


15. [【155】最小栈 - 简单](https://leetcode-cn.com/problems/min-stack/)
   > 以空间换时间的思想，每次在push和pop元素的时候，同步更新一个最小元素的栈。

16. [【189】旋转数组 - 简单](https://leetcode-cn.com/problems/rotate-array/)
   > 1. 解法1: 最后的元素依次插入到数组前面，插入k次(k=k%n)，时间复杂度O(n^2)，空间复杂度O(1)
   > 2. 解法2: 最前的元素依次添加到数组后面，添加n-k次(k=k%n)，时间复杂度O(n^2)，空间复杂度O(1)
   > 3. 解法3: 反转nums[:k]，反转nums[k+1:]，再反转nums，时间复杂度O(n)，空间复杂度O(1)
   题解中部分涉及到nums[:]操作的均为拷贝，没有原地进行修改，个人感觉不符合题目要求。

17. [【206】反转链表 - 简单](https://leetcode-cn.com/problems/reverse-linked-list/)
   > 构建新链表，遍历原链表的同时改变节点的指向

18. [【283】移动零 - 简单](https://leetcode-cn.com/problems/move-zeroes/)
   > 使用快慢双指针，交换两个下标的值，一开始错误将快指针的下标从1开始，导致非零测试样例[1,2]会被错误输出为[2,1]，后续将快指针下标从0开始，该错误解决。

19. [【641】设计循环双端队列 - 中等](https://leetcode-cn.com/problems/design-circular-deque/)
   > 采用数组实现，需要注意的是从头部插入使用的self._front = (self._front - 1)%self._capacity，由于 -1 % 9 = 8可知，从头部插入的实际实现方式是添加到数组末尾，而从尾部插入也是正好相反，实现方式是添加到数组前面。