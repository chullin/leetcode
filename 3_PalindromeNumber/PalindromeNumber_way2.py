class Solution(object):
    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10

        return x == half or x == half // 10


if __name__ == '__main__':
    case1 = Solution()
    input = 12321
    print(case1.isPalindrome(input))