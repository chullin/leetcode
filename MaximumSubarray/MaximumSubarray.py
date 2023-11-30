class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = 0
        for i in range(len(nums)):
            # print(nums[i])
            if max_sum < nums[i]:
                max_sum = nums[i]

            




        return max_sum






if __name__ ==  '__main__':
    case1 = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(case1))