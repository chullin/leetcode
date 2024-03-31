"""
                                                f(0, False)                       🔽 => repeated calculations
					                          /             \ 
                       		       f(1, False)              f(1, True)
			                      /          \       🔽          \      🔽
			                 f(2, False)      f(2, True)           f(2, True)
							/            \  🔽       \   🔽           \  🔽
						f(3, False)   f(3,True)     f(3, True)           f(3, True)
						/        \            \           \                  \
				      ...        ...          ...         ...                ...
"""
from numpy import inf


class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)


if __name__ ==  '__main__':
    case1 = [5,4,-1,7,8]
    solution = Solution()
    print("Max_sum = ", solution.maxSubArray(case1))