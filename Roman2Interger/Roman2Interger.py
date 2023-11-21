def romanToInt(s: str):
        length = len(s)
        Map = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        buf = []
        sum = 0
        for i in range(length):
            # print(Map[s[i]])
            buf.append(Map[s[i]])       
        # for i in range(length):
        #      print('buf = ', buf[i])
            if i == 0:
                sum = Map[s[i]]
                print('sum = ', sum)
            elif buf[i] <= buf[i-1] :
                sum = sum + Map[s[i]]
                print('sum = ', sum)
            else:
                sum = sum + Map[s[i]] - Map[s[i-1]]*2
                print('sum = ', sum)
        return sum
                



if __name__ == '__main__':
    s = "MCMXCIV"           # [1000, 100, 1000, 10, 100, 1, 5]
    print(romanToInt(s))