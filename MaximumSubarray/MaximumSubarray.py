class Solution:
    def maxSubArray(self, nums) -> int:

        Max_sum = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                # print("["+str(i)+"]", "["+str(j)+"]")
                sum += nums[j]
                # print(sum)
                if Max_sum < sum:
                    Max_sum = sum

        return Max_sum



if __name__ ==  '__main__':
    case1 = [5,4,-1,7,8]
    solution = Solution()
    print("Max_sum = ", solution.maxSubArray(case1))