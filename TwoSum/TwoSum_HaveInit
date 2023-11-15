class Solution(object):
    def twoSum(self, nums, target) -> (list, int):
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

# 创建 Solution 类的实例
solution_instance = Solution()

# 定义输入数据
nums = [2, 7, 11, 15]
target = 9

# 调用 twoSum 函数
result = solution_instance.twoSum(nums, target)

# 输出结果
print("Indices of the two numbers:", result)
