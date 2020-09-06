# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其层序遍历: 
# 
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#  
# 
#  
# 
#  说明: 
# 
#  
#  树的深度不会超过 1000。 
#  树的节点总数不会超过 5000。 
#  Related Topics 树 广度优先搜索 
#  👍 107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# # 解法1: 深度优先搜索 DFS
# class Solution:
#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#
#         res = []
#         def dfs(root, depth):
#             if not root:
#                 return
#             # 进入下一层, 初始化
#             if len(res) <= depth:
#                 res.append([])
#             # 由于有depth下标的存在,因此append的时候不会出错
#             res[depth].append(root.val)
#             for ch in root.children:
#                 dfs(ch, depth + 1)
#
#         dfs(root, 0)
#         return res

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
# leetcode submit region end(Prohibit modification and deletion)
