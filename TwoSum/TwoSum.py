class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for y in range(i+1, len(nums)):
                print(nums[i] + nums[y])
                if(nums[i] + nums[y] == target):
                    return i, y


# 創建 Solution 類的實例
solution_instance = Solution()

# 定義輸入資料
nums = [2, 7, 11, 15]
target = 9


# 調用 twoSum 函數
result = solution_instance.twoSum(nums, target)

# 輸出結果
print("Indices of the two numbers:", result)
