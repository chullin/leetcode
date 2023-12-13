"""
result = max(nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False))
這行程式碼為什麼不能寫成下面這樣
result = max(nums[i] + solve(i+1, True), solve(i+1, False))

讓我們使用一個簡單的例子，假設 nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]。

當 must_pick 為 True 時（必須選擇當前元素）：

原始：nums[i] + solve(i + 1, True)，這表示我們選擇了當前的元素，並遞歸計算下一個位置。
修改：nums[i] + solve(i + 1, True)，這也表示相同的行為。
當 must_pick 為 False 時（可以不選擇當前元素）：

原始：0 if must_pick else solve(i + 1, False)，這表示我們沒有選擇當前元素，而是直接遞歸計算下一個位置的結果。
修改：solve(i + 1, False)，這表示我們直接遞歸計算下一個位置的結果。

"""


class Solution:
    def maxSubArray(self, nums):
        memo ={}

        def solve(i, pick: bool):
            if i >= len(nums):
                if pick:
                    return 0
                else:
                    return 0
                # return 0 if pick else float('-inf')

            
            if (i, pick) in memo:
                return memo[(i, pick)]
            
            result = max(nums[i] + solve(i+1, True), solve(i+1, False))
            memo[(i, pick)] = result
            return result
        
        return solve(0, False)
    

def main():
    case1 = [1, 2, 3, 4]
    solution = Solution()
    print("Max_sum = ", solution.maxSubArray(case1))


if __name__ ==  '__main__':
    main()