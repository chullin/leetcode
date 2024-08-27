class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = s
        str2 = t

        arr1 = sorted(list(str1))
        arr2 = sorted(list(str2))

        print("字串一分解並排序後的陣列:", arr1)
        print("字串二分解並排序後的陣列:", arr2)

        if arr1 == arr2:
            return "true"
        else:
            return "false"

Solution_instance = Solution()
input1 = "anagram"
input2 = "nagaram"

result1 = Solution_instance.isAnagram(input1, input2)
print("Result1:", result1) 