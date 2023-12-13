def romanToInt(s: str):
    ans = 0
    num = 0
    for i in range(len(s)-1, -1, -1):
        print('i=', i)
        if s[i] == 'I':
            num = 1
        elif s[i] == 'V':
            num = 5
        elif s[i] == 'X':
            num = 10
        elif s[i] == 'L':
            num = 50
        elif s[i] == 'C':
            num = 100
        elif s[i] == 'D':
            num = 500
        elif s[i] == 'M':
            num = 1000
        
        if 4 * num < ans:
            ans -= num
        else:
            ans += num
    return ans

if __name__ == '__main__':
    s = "MCMXCIV"           # [1000, 100, 1000, 10, 100, 1, 5] = 1994
    print(romanToInt(s))