# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  示例: 
# 
#  你可以将以下二叉树：
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]" 
# 
#  提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
# 个问题。 
# 
#  说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。 
#  Related Topics 树 设计 
#  👍 356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 序列化即可以看做层序遍历
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)
            if not node.left:
                if len(levels) < level + 2:
                    levels.append([])
                levels[level + 1].append(None)

            if not node.right:
                if len(levels) < level + 2:
                    levels.append([])
                levels[level + 1].append(None)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)

            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        # print(levels)

        #  去除末尾连续的None
        res = []
        _ = [res.extend(i) for i in levels if set(i) != {None,}]

        # print(res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 根据列表数据构建二叉树
        # i 的左儿子为 2 * i + 1
        # i 的又右儿子为 2 * i + 2
        if not data or not data[0]:
            return None
        tmp = [TreeNode(i) if i is not None else None for i in data]
        # print(tmp)

        for i, j in enumerate(tmp):
            if 2 * i + 1 < len(tmp):
                # 左儿子
                j.left = tmp[2 * i + 1]
            if 2 * i + 2 < len(tmp):
                # 右儿子
                j.right = tmp[2 * i + 2]

        # print(tmp[0])
        return tmp[0]



        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# Codec.deserialize(Codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
