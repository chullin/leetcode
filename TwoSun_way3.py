'''
Way3: 
    1. 創建一個空字典
    2. 新增一個變數 complement 儲存 target - nums 的當前值
    3. 如果字典裡面沒有 complement 就儲存 nums 的當前值
    4. 直到 complement 與字典中的值相符就回傳


    python 版本太舊不支援 :list 的註解方式, 3.8.2 不支援會報錯
'''
class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]

            if complement in numMap.values():
                return [list(numMap.values()).index(complement), i]
          
            numMap[i] = nums[i]
        return []
    

# Creating instances of the Solution class
solution_instance = Solution()

# Defining Input Data
nums = [2, 7, 11, 15]
target = 9

# Calling the twoSum Function
result = solution_instance.twoSum(nums, target)

# output result
print("Indices of the two numbers:", result)



'''
簡單的例子演示 list(numMap.values()).index(complement) 的實際用法：
    
    假設 numMap = {0: 2, 1: 7, 2: 11}，而 complement = 7。
    numMap.values() 回傳視圖：[2, 7, 11]
    list(...) 將視圖轉換為列表：[2, 7, 11]
    .index(complement) 尋找 complement 在列表中的索引：1
    所以，list(numMap.values()).index(complement) 回傳的是 1，這表示補充值 7 在 numMap 中對應的索引。在這個例子中，補充值 7 對應於鍵 1，因此返回的索引是 1。
    
'''