## 題目：Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true


Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.

# 我的想法
題目很好心的直接將輸入都固定在小寫，這樣轉換成編碼時就不需要在額外轉換

先將字串變成陣列
s = "racecar"
str1 = ["r", "a", "c", "e", "c", "a", "r"]

再將 str1 做排序
變成   ["a", "a", "c", "c", "e", "r", "r"]

再將兩個做完排序的陣列做比對

## 詢問了皓評想法
果然高手想法就是不一樣?
他會計數字串中每個字母的次數，然後將兩個紀錄結果做比對


## 我的作法會牽涉到其他議題
像是：字串轉陣列問題
還有：排序問題

字串轉陣列，在 python 中可以直接使用 list 函式做轉換，有夠方便
而我想的方法居然是 JavaScript 真的被第一個學習的語言影響很深啊

```python
def to_char_array(string):
    char_array = []
    for char in string:
        char_array.append(char)
    return char_array
```

排序，最簡單的是泡泡排序

```python
# 手動實現排序（使用簡單的冒泡排序法）
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # 交換元素
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

最快的排序方式為合併、快速排序法，但快速排序不夠穩定
而 python 中也有內建函數可以用於排序 `sorted()`

而 python 內建函數實作是使用 Timsort 方式排序

## Timsort 
是一種混合排序演算法，由 Tim Peters 在 2002 年設計，專門用於 Python 的排序功能。它結合了「插入排序」和「歸併排序」的優點，特別適合處理實際應用中的數據集，如已經部分排序的數據。

### 內部原理
1. 分割序列： Timsort 會將序列分割成多個小段，稱為 "runs"。這些小段要麼是遞增的，要麼是遞減的。如果是遞減的，它們會被反轉成遞增。

2. 運用插入排序： 對於較小的 "runs" 使用插入排序，因為插入排序在小規模數據上表現得非常高效。

3. 合併排序： 在排序完每個 "runs" 後，Timsort 會像歸併排序一樣將這些 "runs" 合併成更大的排序區間。
