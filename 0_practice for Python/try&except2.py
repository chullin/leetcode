try:
    print(1/0)
except TypeError:
    print('型別發生錯誤')
except NameError:
    print('使用沒有被定義的對象')
except Exception:
    print('不知道怎麼了，反正發生錯誤惹')
    

print('hello')