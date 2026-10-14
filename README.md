# 🐍 LeetCode Practice

使用 Python 練習解題，兼顧基礎能力、面試準備與持續複習。

目前固定練習 **18 題**，每題先掌握一種主要解法。能自行推導、實作並解釋，就可以繼續下一題，同時安排複習。

## 🎯 選題依據

- 參考 [Grind 75 的選題方法](https://www.techinterviewhandbook.org/grind75/faq)、[作者的面試練習計畫](https://www.techinterviewhandbook.org/coding-interview-study-plan/)與[精選題單](https://www.techinterviewhandbook.org/best-practice-questions/)。
- Grind 75 作者的選題綜合考量頻率、公司、題型等因素；本表再依先備知識與目前進度安排順序。
- 特定公司的近期考題頻率**尚未確認**。確定目標公司與職缺後，再依可靠資料調整順序或少量替換。
- 題號、難度與條件以各題 LeetCode 官方頁面為準。

## 🧩 核心練習表

第一輪依序練習；後續優先處理到期複習與弱題。

**先前紀錄：** ✔＝之前做過；△＝之前標記待補強；—＝尚未標記完成。做過不代表目前能獨立完成。

**最近結果：** ◎＝獨立完成；△＝需要方法提示；×＝需要完整解答。每次覆寫最後一欄，例如 `◎／2026-10-20`。

| 順序 | 題目 | 難度 | 主要練習重點 | 先前紀錄 | 最近結果／下次複習 |
| :--: | :-- | :--: | :-- | :--: | :--: |
| 1 | [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | HashMap：值 → 索引；先查再存 | ◎ | 2026-10-21 |
| 2 | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | set：查找與去重 | ✔ | — |
| 3 | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | dict／Counter：頻率計數 | ✔ | — |
| 4 | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | 排序字串作 key；dict 分組 | ✔ | — |
| 5 | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | 頻率計數＋bucket；heap 後補 | △ | — |
| 6 | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Stack：成對匹配與處理順序 | — | — |
| 7 | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | 左右指標；跳過非英數字元 | — | — |
| 8 | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | 單次掃描；維護最低價與最佳利潤 | — | — |
| 9 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Sliding Window：重複時縮小視窗 | — | — |
| 10 | [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | 搜尋區間；邊界與終止條件 | — | — |
| 11 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | 保存下一節點，再改變連結 | — | — |
| 12 | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Dummy node；串接節點 | — | — |
| 13 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | 快慢指標；比較節點身分 | — | — |
| 14 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | DFS：空節點與遞迴回傳值 | — | — |
| 15 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS：deque；逐層處理 | — | — |
| 16 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Graph／Grid traversal：走訪與 visited | — | — |
| 17 | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | DP：狀態、初始值與轉移 | — | — |
| 18 | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Kadane：以目前位置結尾的最佳和 | ✔／DP △ | — |

## 🔁 每次怎麼練習？

1. 打開題目，先不看舊程式、解答或表格中的方法提示。
2. 說明輸入／輸出，選擇資料結構與解法，再用 Python 實作。
3. 檢查一般案例，以及題目允許的邊界案例。
4. 解釋變數保存什麼、更新為什麼正確，以及時間／空間複雜度。
5. 記下這次卡住的一件事，更新表格中的結果與下次複習日期。

卡住約 **10–15 分鐘**仍沒有方向時，先看一個提示；需要完整解答也可以。關掉解答後重寫，當次仍記為 ×，隔天再確認能否獨立完成。

每題先練一種主要解法，理解它與暴力解法的差異即可，不要求同時完成三種解法。

- Group Anagrams：先用排序後的字串作 key，字元計數 key 後補。
- Top K Frequent Elements：先理解頻率計數，再練 bucket；heap／Quickselect 後補。完整排序可作理解起點，但不一定符合官方 follow-up 的複雜度要求。
- Reverse Linked List：先掌握迴圈版本，遞迴版本後補。
- Number of Islands：先掌握一種走訪方法；使用迭代 DFS 或 BFS 可避免深層遞迴的問題。
- Maximum Subarray：先理解 Kadane 的狀態與更新，分治版本後補。

## 📅 複習安排

| 結果 | 判定方式 | 建議下次複習 |
| :--: | :-- | :-- |
| × | 需要完整解答，或仍無法解釋 | 隔天 |
| △ | 需要方法提示，或關鍵步驟／邊界不穩 | 約 3 天後 |
| ◎ | 無方法提示完成，能解釋並檢查案例 | 約 7 天後；再次成功可拉長到 14 天 |

以上間隔是執行起點，依實際表現調整。單純查 Python API 拼法，另外記為語法卡點；靠提示才選出解題方法，就記為 △。

每天先保留約 **30 分鐘**：

- 優先複習一題到期的舊題。
- 還有時間，再做下一題或補強弱題；一題就用完時間也可以。
- 穩定的題目拉長複習間隔，弱題優先。
- 每週挑一次，遮住方法欄、混合類別抽題，練習自行辨認解題模式。

## 🚀 何時調整清單？

**同一類的基礎題能獨立完成並解釋，就可以加入對應的進階題；不用等全部 18 題都非常熟練。**

目標公司明確後：

1. 先確認資料的公司、職缺、時間範圍與來源；查不到就標示「頻率未確認」。
2. 本表與公司常見題重疊的項目，優先練習與複習。
3. 本表以外、但已具備先備知識的題目，可加入或替換一題。
4. 尚缺基礎的題目，先補對應基礎，再練該題。
5. 每次只調整少量題目，固定練習範圍維持約 18–20 題。

LeetCode [官方說明](https://support.leetcode.com/hc/en-us/articles/360011985113-How-does-grouping-questions-by-company-work)：公司題目列表來自使用者的面試回報。使用時需留意其與目標職缺的關聯。

<details>
<summary>📂 已完成但暫不固定複刷的題目</summary>

以下沿用原本的完成紀錄，保留成果，需要時再回來練習：

- ✔ [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- ✔ [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- ✔ [27. Remove Element](https://leetcode.com/problems/remove-element/)
- ✔ [169. Majority Element](https://leetcode.com/problems/majority-element/)
- ✔ [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- ✔ [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

</details>

<details>
<summary>📚 後續擴充與 Python 參考</summary>

- Invert Binary Tree：需要更多 Tree 遞迴練習時再加入。
- 其他題目依基礎掌握程度與目標公司資料逐批加入；原本的 Top 50 與 14 天計畫不另行維護。
- [Python Functions — Quizlet](https://quizlet.com/tw/938125480/python-%E5%87%BD%E6%95%B8-flash-cards)

</details>
