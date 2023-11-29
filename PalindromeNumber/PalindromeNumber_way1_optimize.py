class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]
    

if __name__ == '__main__':
    instance = Solution()
    input_value = 123454321
    print(instance.isPalindrome(input_value))