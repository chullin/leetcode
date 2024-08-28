class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        minus_dict = {}
        for i, num in enumerate(nums):
            minus = target - num
            if minus in minus_dict:
                return [minus_dict[minus], i]
            minus_dict[num] = i




Solution_instance = Solution()
input1 = [2,11,7,15]
target1 = 9
print(Solution_instance.twoSum(input1, target1)) # [0,1]