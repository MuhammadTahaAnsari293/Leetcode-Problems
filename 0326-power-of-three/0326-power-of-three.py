class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True # base case
        elif n == 0:
            return False # special case
        elif n % 3 != 0:
            return False
        return self.isPowerOfThree(n//3)
        