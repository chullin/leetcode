'''
Way2: 先將 nums 編號並存在字典中，
    然後用 target - nums 的當前值
    最後看扣完的值是否存在 nums 中
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            
            # complement should be in numMap, but not the same object, so can not be equal to i
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
    

# Creating instances of the Solution class
solution_instance = Solution()

# Defining Input Data
nums = [2, 7, 11, 15]
target = 9

# Calling the twoSum Function
result = solution_instance.twoSum(nums, target)

# output result
print("Indices of the two numbers:", result)