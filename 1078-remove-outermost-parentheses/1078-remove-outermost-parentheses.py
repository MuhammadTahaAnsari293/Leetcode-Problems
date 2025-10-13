class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=''
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
                if len(stack)>1:
                    res+=s[i]
            elif s[i]==')':
                if len(stack)>1:
                    res+=s[i]
                stack.pop()
        return res
        