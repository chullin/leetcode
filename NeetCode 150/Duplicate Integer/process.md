題目：[Duplicate Integer](https://neetcode.io/problems/duplicate-integer)

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

簡單的想法，把讀到的第一個值存起來，然後依序跟後面的 2、3、4 去比較，如果一樣就輸出 ture，如果比到最後都沒找到，就輸出 false

第二個版本是 Coplite 跳出來的語法，是專屬於 python 的快速寫法

天啊，在 Neetcode Solution 影片中給的解答，真的令我無法想像，居然還有這樣的想法
上面我寫了兩個方法，其實都只是屬於暴力破解，對於演算法來說是一模一樣的，計算複雜度都是 O(n^2)

第二種演算法：
1. 先將輸入進來的陣列排序，這樣就只需要比對相鄰的元素
2. 使用兩個指標，或是陣列...都可以，進行比對，兩個兩個比對

這樣計算複雜度就會下降至 O(log n)


然後是我完全看不懂的第三種：
使用的是 Hashset，將輸入進來的數字都讀到 Hashset 裡面

Python 內建的 set 類型本質上就是使用哈希表來實現的，因此它可以被視為一種 HashSet。
特性：
1. 唯一性：集合中的元素是唯一的，不能有重複值。
2. 無序性：集合中的元素沒有特定的順序。
3. 基於哈希：集合使用哈希表實現，因此查找、插入和刪除的時間複雜度通常是 O(1)。


在 Python 中，set 的操作之所以可以達到平均時間複雜度 O(1)，是因為它背後使用了哈希表 (hash table) 的資料結構。以下是原因：

1. 哈希表的結構：
哈希表是一種將「鍵」(key) 映射到「值」(value) 的資料結構。在集合 (set) 中，只有鍵沒有值，因此每個元素就是集合中的一個鍵。
當你將一個元素放入集合時，Python 會根據該元素的哈希值（由 hash() 函數計算）決定該元素應該存放在哈希表的哪個位置。
2. 快速定位：
透過哈希值，哈希表能夠直接計算出元素在內存中的位置，而不需要遍歷整個集合。因此，插入、刪除和查找元素都只需一步即可完成，這使得這些操作的平均時間複雜度是 O(1)。

# 解答：
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```