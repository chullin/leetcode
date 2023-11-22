def romanToInt(s: str):
        length = len(s)
        Map = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and Map[s[i]] < Map[s[i+1]]:
                ans -= Map[s[i]]
            else:
                ans += Map[s[i]]
                
        return ans


if __name__ == '__main__':
    s = "MCMXCIV"           # [1000, 100, 1000, 10, 100, 1, 5] = 1994
    print(romanToInt(s))