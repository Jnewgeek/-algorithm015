# 给定一个 N 叉树，返回其节点值的前序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其前序遍历: [1,3,5,6,2,4]。 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#递归算法，使用缓存记录已经经过的节点，空间换时间
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

# 2. 迭代算法, 执行效率低于迭代算法
# class Solution:
#
#     def preorder(self, root: 'Node') -> List[int]:
#         white, gray = 0, 1
#         stack, res = [(white,root)], []
#         while stack:
#             color, node = stack.pop()
#             if node is None:
#                 continue
#             if color == white:
#                 if isinstance(node.children, list):
#                     for i in node.children[::-1]:
#                         stack.append((white, i))
#                 else:
#                     stack.append((white,node.children))
#                 stack.append((gray, node.val))
#             else:
#                 res.append(node)
#         return res
# leetcode submit region end(Prohibit modification and deletion)
