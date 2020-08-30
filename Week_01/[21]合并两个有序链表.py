# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1238 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        nodes=[]
        for l in [l1, l2]:
            while l:
                nodes.append(l.val)
                l = l.next

        res = cur = ListNode(-1)
        for i in sorted(nodes):
            cur.next = ListNode(i)
            cur = cur.next

        return res.next
        
# leetcode submit region end(Prohibit modification and deletion)
