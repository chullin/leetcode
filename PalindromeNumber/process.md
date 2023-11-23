在 leetcode 中要使用 return 返回 Ture 和 false
看到題目寫小寫的直接被混淆
結果簡單的題目費時 1小時半

原本想了 3 個方法，但發現好像有兩個沒有用
1. 使用 queue ，先 queue 進來，然後在 pop 出去比對
   但發現這樣很多餘，一樣要儲存，並且很麻煩，所以放棄
2. 使用兩個 flag，一個指頭，一個指尾
   原本以為可以不用額外儲存空間，但好像只有 C 才有這種功能， python 一樣要用兩個陣列，所以跟但三種方法好像沒差到哪去
3. 反轉第二個陣列，然後比較到長度一半的地方

我在這個題目中遇到的困難點
 * 題目中 input 有正數和負數，輸入前要先使用陣列儲存，記住這個方法 ```[str(i) for i in str(x)]```，語法內容是先 str(x) 到 i 中，然後使用 str 去除存，原本是 int(i)，但輸入中有負號，所以會錯
 * reverse() 換會改變原本的資料，所以 input2 要先 copy 再 reverse
 * 5/2 照理來說是 3，但 python 會讓輸出變 2，因為輸出比較接近 2，所以要使用 math 函數中的無條件進位，先 import math，然後使用 ceil 函數，然後因為只會有 0.5 的問題，所以直接進位就對了
 * 最後就是一開始說的，居然要用 return 的，我用 print 所以輸出對也是一直錯


我的 code Runtime: 69ms

別人的解答：Runtime: 67 ms 還行，差不多，雖然輸了 2ms