# 给定一个二叉树，返回它的 前序 遍历。 
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
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 357 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1: 递归算法
# class Solution:
#
#     def __init__(self):
#         self.res = []
#
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root:
#             self.res.append(root.val)
#             self.preorderTraversal(root.left)
#             self.preorderTraversal(root.right)
#         return self.res

# 解法2: 迭代算法
class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.left, node.val])
            elif isinstance(node, int):
                res.append(node)
            else:
                continue

        return res
# leetcode submit region end(Prohibit modification and deletion)
