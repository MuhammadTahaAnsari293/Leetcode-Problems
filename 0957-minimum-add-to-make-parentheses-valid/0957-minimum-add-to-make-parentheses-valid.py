class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if not stack: # just to add first element
                stack.append(i)
            elif i == ")" and stack[-1]=="(": # to check valid parentheses
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
            

        