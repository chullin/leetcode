try:
    a = int(input('輸入 0~9: '))
    if a>10:
        raise
    print(a)
except :
    print('有錯誤喔～')
else:
    print('沒有錯！繼續執行！')       # 完全沒錯才會執行這行
finally:
    print('管他有沒有錯，繼續啦！')    # 不論有沒有錯都會執行這行 