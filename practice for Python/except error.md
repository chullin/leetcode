參考資料：https://steam.oxxostudio.tw/category/python/basic/try-except.html

寫的不錯欸!

except 的錯誤資訊 
只要程式發生錯誤，控制台中都會出現對應的錯誤資訊，下方列出常見的幾種錯誤資訊 ( 詳細錯誤資訊參考：Built-in Exceptions )：


|錯誤資訊 | 說明 |
| :---:| :---: | 
NameError | 使用沒有被定義的對象
IndexError | 索引值超過了序列的大小
TypeError |	數據類型 ( type ) 錯誤
SyntaxError	Python | 語法規則錯誤
ValueError | 傳入值錯誤
KeyboardInterrupt | 當程式被手動強制中止
AssertionError | 程式 asset 後面的條件不成立
KeyError | 鍵發生錯誤
ZeroDivisionError | 除以 0
AttributeError | 使用不存在的屬性
IndentationError | Python 語法錯誤 ( 沒有對齊 )
IOError | Input/output異常
UnboundLocalError | 區域變數和全域變數發生重複或錯誤



try&except.py
* 使用 try 和 except 

try&except2.py
* 加入更多種類的 Error 類別

try&except3.py
* 加入自定義 Error 類別

try&except4.py
* 加入 else 和 finally 
