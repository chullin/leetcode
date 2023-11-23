class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        input = [str(i) for i in str(x)]
        input2 = input.copy()
        input2.reverse()

        # for i in range(len(input)):
        #     print(input[i])
        #     print('---')

        # for i in range(len(input)-1, -1, -1):
        #     print(input2[i])

        for i in range(math.ceil(len(input)/2)):
            # print(round(len(input)/2))
            if input[i] != input2[i]:
                    print("False")
                    break
            else:
                if i == math.ceil(len(input)/2)-1:
                    print("True")

if __name__ == '__main__':
    Solution().isPalindrome(121)