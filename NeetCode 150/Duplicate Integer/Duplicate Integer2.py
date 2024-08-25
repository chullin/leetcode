class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        tag = None
        for i in range(len(nums)):
            tag = nums[i]
            if tag in nums[i+1:]:
                return True
        return False


Solution_instance = Solution()

nums1 = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

result1 = Solution_instance.hasDuplicate(nums1)
result2 = Solution_instance.hasDuplicate(nums2)

print("Result1:", result1)
print("Result2:", result2)