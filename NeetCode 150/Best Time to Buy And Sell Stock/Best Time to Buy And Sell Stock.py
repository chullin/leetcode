class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = prices[0]
        profit = 0
        for i in prices:
            if i < min:
                min = i
            else:
                profit = max(profit, i - min)
        return profit

Solution_instance = Solution()

Input1 = [10,1,5,6,7,1]
Input2 = [10,8,7,5,2]

result1 = Solution_instance.maxProfit(Input1)
result2 = Solution_instance.maxProfit(Input2)

print("Result1:", result1)
print("Result2:", result2)