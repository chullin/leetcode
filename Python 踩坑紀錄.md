## Python 踩坑紀錄

### 27 題

`nums = new_nums` 在 Python 中，他只是改了「區域變數指向」
Python 是：👉 pass by object reference（傳參考）
👉 沒有改到原本那個 list
!! 要用切片才可以改掉原本的陣列 !!
像是這樣 `nums[:] = new_nums`

### 3643 題

Python 除法 `9//2 = 4` 只取整數
如果要用 floor 或是 ceil 函式，需要 import math
四捨五入：
round() 可能會因為浮點數問題而不按預期運作
round(2.5) -> 2, round(3.5) -> 4
`list[a], list[b] = list[b], list[a]`
Python 中特殊的寫法，他會先處理右邊，然後包成 tuple
然後同時 assign 到左邊

### 88 題

non-decreasing order 是已經排好序的了
in-place 在原本的陣列裡面

### 80 題

也是需要兩個指針，一個是 slow、一個是 fast
因為一個元素最多只能出現兩次，因此陣列的前面兩個元素就可以忽略，
因為不管出現什麼都不會有影響
要想題目在什麼條件會出問題

### 217 題

「資料結構思維」的入門經典
會用 set 超簡單，不會用 set 怎麼寫都很複雜
Python 特有函數: set()

👉 set 是「只存值」
👉 dict（dictionary）是「key → value 對應」

##### 特性：

- 只有「值」，沒有 key
- 不允許重複
- 無序（不能用 index 取值）

👉 自動去重！

```python
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}
```

#### 容易搞混！！

| 寫法        | 類型  | 可變？    |
| ----------- | ----- | --------- |
| `(1, 2, 3)` | tuple | ❌ 不可變 |
| `{1, 2, 3}` | set   | ✅ 可變   |
| `[1, 2, 3]` | list  | ✅ 可變   |

#### set vs. dict

| 寫法        | 類型    |
| ----------- | ------- |
| `{}`        | ❌ dict |
| `{1, 2, 3}` | ✅ set  |
| `{"a": 1}`  | ✅ dict |
| `set()`     | ✅ set  |

#### Set 常見用途

- 去重
- 判斷是否存在（速度很快）

```python
  nums = [1, 2, 2, 3]
  unique = set(nums)  # {1, 2, 3}
```

#### set 常見方法

以下都是 python 內建函式

```python
set.add()
set.remove()    # 如果不存在會報錯
set.discard()   # 如果不存在不會進行任何操作
```
