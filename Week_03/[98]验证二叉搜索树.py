# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 
#  👍 759 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1: 在中序遍历的基础上进行修改,只要当前节点的元素小于等于前一个元素,则提前终止,该树不是二叉搜索树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历, 记录前一个数, 只要后一个数小于前一个数,即不是二叉搜索树
        if not root:
            return True

        self.pre_val = float('-inf')  # 初始化第一个数
        self.flag = True

        def inorder(root):
            if not self.flag:      # 提前终止
                return
            if root:
                inorder(root.left)
                if root.val <= self.pre_val:
                    self.flag = False
                    return
                self.pre_val = root.val
                inorder(root.right)
            return

        inorder(root)
        return self.flag

# 解法2: 维护一个栈
# class Solution:
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         stack, inorder = [], float('-inf')
#
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             if root.val <= inorder:
#                 return False
#             inorder = root.val
#             root = root.right
#
#         return True
# leetcode submit region end(Prohibit modification and deletion)
