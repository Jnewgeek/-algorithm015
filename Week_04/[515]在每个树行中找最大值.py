# 您需要在二叉树的每一行中找到最大的值。 
# 
#  示例： 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# 输出: [1, 3, 9]
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 91 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue, res = [root], []
        while queue:
            children = []
            _max = float('-inf')
            for node in queue:
                _max = max(_max, node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            queue = children
            res.append(_max)
        return res
# leetcode submit region end(Prohibit modification and deletion)
