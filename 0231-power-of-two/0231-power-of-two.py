class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True # base case
        elif n % 2 !=0:
            return False
        elif n == 0:
            return False
        return self.isPowerOfTwo(n//2) # Recursive Call
        