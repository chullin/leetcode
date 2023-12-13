try:
    a = int(input('輸入 0~9: '))
    if a>9:                 # 如果輸入的 a 大於 9
        #raise              # 強制中斷，拋出錯誤資訊
        raise ValueError('數字不在範圍內')
    print(a)


except ValueError as msg:   # # 如果輸入範圍外的數字或解析非 10 進位數字，執行這邊的程式
    print(msg)  

except :                    # 一定要放在最後一個
    print('有錯誤喔～')      # 收到錯誤訊息，顯示錯誤

print('執行結束')