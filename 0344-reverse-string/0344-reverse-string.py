class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        return self.helper(s, left, right)

    def helper(self, s, left, right):
        if left > right:
            return None
        s[left],s[right]=s[right],s[left]
        return self.helper(s, left+1, right-1)
        