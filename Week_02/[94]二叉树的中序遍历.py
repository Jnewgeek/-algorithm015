# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 659 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1: 递归
# class Solution:
#     def __init__(self):
#         self.res=[]
#
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if root:
#             self.inorderTraversal(root.left)
#             self.res.append(root.val)
#             self.inorderTraversal(root.right)
#
#         return self.res

# 解法2: 迭代，手动维护栈
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

# leetcode submit region end(Prohibit modification and deletion)
