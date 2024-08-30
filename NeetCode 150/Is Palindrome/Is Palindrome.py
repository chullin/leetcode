class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr  = []
        arr2 = []
        input1 = s.lower()
        for i in input1:
            if i >= "A" and i <= "z":
                arr.append(i)
                # print(arr)
        for i in reversed(arr):
            if i >= "A" and i <= "z":
                arr2.append(i)
                # print(arr2)
        for i in range(len(arr)):
            if arr[i] == arr2[i]:
                pass
            else:
                return False
        return True

Solution_instance = Solution()
input1 = "Was it a car or a cat I saw?"
print(Solution_instance.isPalindrome(input1)) # True
input2 = "tab a cat"
print(Solution_instance.isPalindrome(input2)) # True