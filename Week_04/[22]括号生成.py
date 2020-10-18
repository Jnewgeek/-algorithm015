# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1315 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n):
        if n <= 0: return []
        queue, res = [(0, 0, '')], []
        while queue:
            left, right, tmp = queue.pop()
            if left == right == n:
                res.append(tmp)
            if left < n:
                queue.append((left + 1, right, tmp + '('))
            if left > right:
                queue.append((left, right + 1, tmp + ')'))
        return res
# leetcode submit region end(Prohibit modification and deletion)

class Solution:
    def largestRectangleArea(self, n, heights):
        max_area = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height_index = stack.pop()
                max_area = max(max_area, (i - stack[-1] -1) * heights[height_index])

            stack.append(i)

        return max_area

t = Solution()
print(t.largestRectangleArea(5, [1,2,3,4,5]))


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.end_of_word] = self.end_of_word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True



# Your Trie object will be instantiated and called as such:

opts, words = ["Trie","insert","search","search","startsWith","insert","search"], [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
for opt, word in zip(opts, words):
    if opt == 'Trie':
        obj = Trie()
    elif opt == 'insert':
        obj.insert(word[0])
    elif opt == 'search':
        param_2 = obj.search(word[0])
        print('search',word[0], param_2)
    else:
        prefix = word[0]
        param_2 = obj.startsWith(prefix)
        print('startsWith',prefix, param_2)
print(obj.root)