# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索 
#  👍 442 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList):
            return 0
        size, general_dict = len(beginWord), defaultdict(list)
        for w in wordList:
            for i in range(size):
                general_dict[w[:i] + '*' + w[i+1:]].append(w)

        queue = deque()
        queue.append((beginWord, 1))
        mark = defaultdict(bool)
        mark[beginWord] = True

        while queue:
            node, step = queue.popleft()
            if node == endWord:
                return step
            for i in range(size):
                for neighbor in general_dict[node[:i] + '*' + node[i+1:]]:
                    if not mark[neighbor]:
                        mark[neighbor] = True
                        queue.append((neighbor, step + 1))

        return 0
# leetcode submit region end(Prohibit modification and deletion)
