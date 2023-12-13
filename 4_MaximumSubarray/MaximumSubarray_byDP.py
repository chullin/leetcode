"""
solve(i + 1, True) 和 solve(i + 1, False) 
是遞迴呼叫，分別表示選擇和不選擇下一個位置的數字所能得到的最大子數組和。

                                                f(0, False)                       🔽 => repeated calculations
					                          /             \                     false => 不選
                       		       f(1, False)              f(1, True)            true  => 選
			                      /          \       🔽          \      🔽
			                 f(2, False)      f(2, True)           f(2, True)
							/            \  🔽       \   🔽           \  🔽
						f(3, False)   f(3,True)     f(3, True)           f(3, True)
						/        \            \           \                  \
				      ...        ...          ...         ...                ...

>>> me = {}
>>> me[0] = 10
>>> me[1] = 20
>>> me[2] = 30
>>> me[(0, True)] = 10
>>> me[(0, False)] = 20                      
>>> me
{0: 10, 1: 20, 2: 30, (0, True): 10, (0, False): 20}                      
python 的字典功能會不會太困難
"""


class Solution:
    def maxSubArray(self, nums):
        memo = {}

        def solve(i, must_pick):
            # print(i)
            # print(nums)
            if i >= len(nums):
                return 0 if must_pick else float('-inf')

            if (i, must_pick) in memo:
                print(i, must_pick)
                return memo[(i, must_pick)]

                   # max(x, y, ...) => output: Max number
            result = max(nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False))
            memo[(i, must_pick)] = result
            return result

        return solve(0, False)



def main():
    case1 = [1, 2, 3, 4]
    solution = Solution()
    print("Max_sum = ", solution.maxSubArray(case1))


if __name__ ==  '__main__':
    main()