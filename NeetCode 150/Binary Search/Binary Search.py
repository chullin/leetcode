class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # "//" is mean round down
            mid = (right - left) // 2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
Solution_instance = Solution()
Input1 = [-1,0,3,5,9,12]
Input2 = 9
Input3 = 2
print(Solution_instance.search(Input1, Input2))
print(Solution_instance.search(Input1, Input3))