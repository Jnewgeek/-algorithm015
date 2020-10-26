## Week 8

### 位运算

1. **位运算符**
   1. `左移`：<<
   2. `右移`：>>
   3. `按位与`：&
   4. `按位或`：|
   5. `按位取反`：~
   6. `按位异或`：^
2. **XOR-异或高级操作**
   1. x ^ 0 = x
   2. x ^ 1s = ~x     // 1s = ~0  全为1
   3. x ^ (~x) =  1s
   4. x ^ x = 0
   5. c = a ^ b   ==>  a ^ c = b, a ^ b = c    // 交换两个数
   6. a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c    // 满足结合律
3.  **指定位置的位运算**
   1. 将x最右边的n位清零：x & (~0 << n)
   2. 获取x的第n位值(0或者1)：(x >> n) & 1
   3. 获取x的第n位的幂值：x & (1 << n)
   4. 仅将第n位置为1：x | (1 << n)
   5. 仅将第n位置为0：x & (~(1 << n))
   6. 将最高位至第n位(含)清零： x & ((1 << n) - 1)
4. **实战位运算要点**
   1. 判断奇偶：x & 1 == 1 ?
   2. 除2：x  >>= 1  ==>  x /= 2
   3. 清零最低位的1：x &= (x - 1)
   4. 得到最低位的1：p = x & -x
   5. 全部清零：x & ~x = 0

#### 布隆过滤器和LRU缓存

#### 1 布隆过滤器实现代码示例

```python
# Python 
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

#### 2 LRU Cashe Python

```python
class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

### 初级排序

1. 选择排序
2. 插入排序
3. 冒泡排序

**带程序计时和自定义测试案例的初级排序模块**

通过一些测试样例，发现同样的数据量，冒泡法的耗时最长。

```python
import time
import numpy as np
class Solution:

    def __init__(self, nums):
        self.nums = nums

    # 选择排序
    def selectsort(self, reverse = False):
        '''
        每次将最小的值添加的结果中
        :return: 从小到大的排序结果
        '''
        if not self.nums:
            return []
        nums = self.nums[:]
        n = len(nums)
        self.res = []
        while nums:
            min_, index_ = nums[0], 0
            for j in range(index_ + 1, len(nums)):
                if nums[j] < min_:
                    min_, index_ = nums[j], j
            self.res.append(nums.pop(index_))

        return self.res if not reverse else self.res[::-1]

    # 插入排序
    def insertsort(self, reverse = False):
        '''
        预先排好一部分数，遍历未排序的数组，将nums[i]插入到排好序的结果中。
        :return: 从小到大的排序结果
        '''
        if not self.nums:
            return []
        self.res = [self.nums[0]]
        i = 1
        while i < len(self.nums):
            flag = 0               # 只插入一次
            for j, k in enumerate(self.res):
                if self.nums[i] < k:
                    self.res.insert(j, self.nums[i])
                    flag = 1
                    break
            if not flag:
                self.res.append(self.nums[i])
            i += 1
        return self.res if not reverse else self.res[::-1]

    # 冒泡排序
    def bubblesort(self, reverse = False):
        if not self.nums:
            return []
        self.res = self.nums[:]
        for i in range(len(self.res) - 1):
            for j in range(i, len(self.res)):
                if self.res[j] < self.res[i]:
                    self.res[i], self.res[j] = self.res[j], self.res[i]
        return self.res if not reverse else self.res[::-1]

def count_time(func):
    '''
    程序计时
    '''
    def init_time(*args, **kwargs):
        start_time = time.time()
        func()
        over_time = time.time()
        print("用时: %.2fs"%(over_time - start_time))
    return init_time


if __name__ == '__main__':
    nums = list(np.random.randint(100, size = 10000))
    print("Oringin: ", nums)
    t = Solution(nums)
    for solute in [t.selectsort, t.insertsort, t.bubblesort]:
        @count_time
        def main():
            print(solute.__name__, ":", solute())
        main()
```

