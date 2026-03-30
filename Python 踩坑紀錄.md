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
