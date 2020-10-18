## week07

### 1、字典树和并查集

> 字典树，即Trie树，又称单词查找树或键树，是一种树形结构，经常用作搜索引擎。最大限度地减少无谓的字符串比较，查询效率比哈希表高。
>
> 核心思想：空间换时间，以单词为例：不区分大小写的情况下，最坏情况下为26叉树，单词长度最长可能在10左右，因此树的深度最深为10左右。 

**Trie树代码模板**

```python
def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

单词搜索II时间复杂度：

(1) words遍历 ——> search

O(N\*m\*m\*4^k)   N为words数组长度，m为网格长度，k为word平均长度

(2)Trie树

O(m\*m\*4^k)   m为trie树第一层键的长度，k为word平均长度

**并查集代码模板**

```python
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```

### 2、高级搜索

- 剪枝

- 双向BFS

- 启发式搜索

**初级搜索**

1. 朴素搜索

2. 优化方式：不重复(fibonacci)，剪枝(生成括号问题)

3. 搜索方向：

   DFS: depth first search 深度优先

   BFS: breadth first search 广度优先

   双向搜索，启发式搜索

*零钱置换状态树*

DFS 代码 - 递归写法

```python
#Python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

非递归写法

```python
#Python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```

BFS 代码

```python
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```









