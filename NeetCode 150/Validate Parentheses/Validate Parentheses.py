class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {')':'(', 
               '}':'{', 
               ']':'['}
        for i in s:
            if i not in Map:
                stack.append(i)
                continue
            if stack is None or Map[i] != stack.pop():
                return False

        return not stack


Solution_instance = Solution()
Input1 = "[]"
Input2 = "([{}])"
Input3 = "[(])"
Input4 = "["

print(Solution_instance.isValid(Input1))
print(Solution_instance.isValid(Input2))
print(Solution_instance.isValid(Input3))
print(Solution_instance.isValid(Input4))
