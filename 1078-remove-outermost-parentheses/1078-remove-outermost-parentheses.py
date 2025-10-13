class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack1 = [] # to determine valid parantheses
        stack2 = [] # to remove outer parantheses of valid
        stack3 = [] # answer
        for char in s: # the loop must be stop when a valid is found and further actions continue
            stack2.append(char)
            if char == "(":
                stack1.append(")")
            elif char == ")":
                stack1.pop()
            while not stack1 and stack2:
                stack2.pop()
                for _ in range(len(stack2)):
                    stack1.append(stack2.pop())
                stack1.pop()
                for _ in range(len(stack1)):
                    stack3.append(stack1.pop())
        return "".join(stack3)
        