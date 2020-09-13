# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
#  Related Topics 树 深度优先搜索 
#  👍 697 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1: 前序遍历
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0

        def preorder(root, depth):
            if root:
                self.depth = max(self.depth, depth)
                preorder(root.left, depth + 1)
                preorder(root.right, depth + 1)
            return

        preorder(root, 1)
        return self.depth

# 解法2: 深度优先  自底向上
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def bottom_up(node):
            return 0 if node is None else max(bottom_up(node.left), bottom_up(node.right)) + 1
        return bottom_up(root)

# 解法3: 深度优先 自顶向下
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def top_down(node, h):
            return h if node is None else max(top_down(node.left, h + 1), top_down(node.right, h + 1))
        return top_down(root, 0)
# leetcode submit region end(Prohibit modification and deletion)
